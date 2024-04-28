import os
import json
import base64
import requests
import traceback
from flask import request, jsonify
from werkzeug.utils import secure_filename
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.exceptions import BadRequest

from config import Config
from llm.assistant import Assistant
from api.utils.file import allowed_file
from api.utils.w2_form import format, format_for_llm
from api.utils.handle_api_errors import handle_api_errors
from constants import VERYFI_W2_API_ENDPOINT, UPLOAD_FOLDER

from database.repositories.user import UserRepository
from database.repositories.w2_form import W2FormRepository
from database.repositories.employee import EmployeeRepository
from database.repositories.employer import EmployerRepository
from database.repositories.tax_information import TaxInformationRepository

class W2Form:
    def __init__(self):
        self.assistant = Assistant()
        self.user_repo = UserRepository()
        self.w2_form_repo = W2FormRepository()
        self.employee_repo = EmployeeRepository()
        self.employer_repo = EmployerRepository()
        self.tax_info_repo = TaxInformationRepository()

    @handle_api_errors
    def upload(self):
        try:
            if "file" not in request.files:
                raise BadRequest("file is required!")

            file = request.files["file"]
            if file.filename == "":
                raise BadRequest("No file selected for uploading!")
            if not allowed_file(file.filename):
                raise BadRequest("Uploaded file type is not allowed!")

            user_id = request.form.get("user_id")
            if not user_id:
                raise BadRequest("user_id is required!")

            user = self.user_repo.get_user_by_id(user_id)
            if user is None:
                raise BadRequest("User not found!")

            file_content = file.read()
            encoded_file = base64.b64encode(file_content).decode("utf-8")

            filename = secure_filename(file.filename)
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(file_path)

            payload = json.dumps(
                {"file_data": encoded_file, "file_name": file.filename}
            )

            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "CLIENT-ID": Config.VERYFI_CLIENT_ID,
                "AUTHORIZATION": Config.VERYFI_API_KEY,
            }

            response = requests.post(
                VERYFI_W2_API_ENDPOINT, headers=headers, data=payload
            )

            if response.status_code == 201:
                data = response.json()
                w2_form_id = self.saveW2Data(data, filename, file_path, user_id)

                w2_forms = self.w2_form_repo.fetch_w2_data_for_user(user_id)
                formatted_data = format_for_llm(w2_forms)
                assistant = self.assistant.create_assistant(formatted_data)
                thread = self.assistant.create_thread()

                self.w2_form_repo.update_w2_form(
                    w2_form_id,
                    {"gpt_assistant_id": assistant.id, "gpt_thread_id": thread.id},
                )

                return (
                    jsonify(
                        {
                            "message": "File successfully processed and data stored",
                            "data": format(w2_forms),
                        }
                    ),
                    200,
                )
            else:
                return (
                    jsonify(
                        {
                            "message": f"Failed to process file: {response.content}",
                            "data": None,
                        }
                    ),
                    response.status_code,
                )
        except SQLAlchemyError as e:
            print(f"An SQLAlchemyError occurred: {type(e).__name__} - {str(e)}")
            traceback.print_exc()
            return jsonify({"error": "Database error occurred!"}), 500

    def saveW2Data(self, data, filename, file_path, user_id):
        employer = self.employer_repo.upsert_employer(
            {
                "name": data["employer_name"],
                "address": data["employer_address"],
                "state_id": data["employer_state_id"],
                "ein": data["ein"],
            },
            flush=True,
        )
        employee = self.employee_repo.upsert_employee(
            {
                "name": data["employee_name"],
                "ssn": data["employee_ssn"],
                "address": data["employee_address"],
            },
            flush=True,
        )
        w2_form = self.w2_form_repo.add_w2_form(
            {
                "user_id": user_id,
                "employer_id": employer.id,
                "employee_id": employee.id,
                "file_name": filename,
                "file_path": file_path,
            },
            flush=True,
        )
        self.tax_info_repo.add_tax_information(
            {
                "w2_form_id": w2_form.id,
                "federal_income_tax": data["federal_income_tax"],
                "state_income_tax": data["state_income_tax"],
                "medicare_tax": data["medicare_tax"],
                "ss_tax": data["ss_tax"],
                "medicare_wages": data["medicare_wages"],
                "ss_wages": data["ss_wages"],
                "state_wages_tips": data["state_wages_tips"],
            }
        )
        return w2_form.id

    @handle_api_errors
    def fetch_w2_data_for_user(self, user_id):
        w2_forms = self.w2_form_repo.fetch_w2_data_for_user(user_id)
        return (
            jsonify(
                {"message": "W2 Forms retrieved successfully", "data": format(w2_forms)}
            ),
            200,
        )
