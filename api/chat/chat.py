from flask import request, jsonify
from datetime import datetime, timezone
from werkzeug.exceptions import BadRequest
from flask_jwt_extended import get_jwt_identity

from llm.assistant import Assistant
from api.chat.validations import AskQuestionSchema
from api.utils.handle_api_errors import handle_api_errors
from database.repositories.user import UserRepository
from database.repositories.w2_form import W2FormRepository

class Chat:
    def __init__(self):
        self.assistant = Assistant()
        self.user_repo = UserRepository()
        self.w2_form_repo = W2FormRepository()

    @handle_api_errors
    def question(self):
        data = AskQuestionSchema(**request.json)

        user_id = get_jwt_identity()
        user = self.user_repo.get_user_by_id(user_id)
        if user is None:
            raise BadRequest("User not found!")

        w2_form = self.w2_form_repo.get_w2_form_by_id(data.w2_form_id)
        if w2_form is None:
            raise BadRequest("W2 Form not found!")

        messages = self.assistant.answer_question(
            data.question, data.gpt_assistant_id, data.gpt_thread_id
        )
        answer = messages.data[0].content[0].text.value
        created_at = (
            datetime.fromtimestamp(messages.data[0].created_at)
            .replace(tzinfo=timezone.utc)
            .isoformat()
        )

        return (
            jsonify(
                {
                    "message": "Answer fetched successfully!",
                    "data": {
                        "message": answer,
                        "created_at": created_at,
                        "role": messages.data[0].role,
                    },
                }
            ),
            200,
        )

    @handle_api_errors
    def get_messages(self, gpt_thread_id):
        thread = self.assistant.retrieve_thread(gpt_thread_id)
        if thread is None:
            raise BadRequest("Thread not found!")

        messages = self.assistant.retrieve_thread_messages(gpt_thread_id)
        sorted_messages = sorted(
            messages.data, key=lambda x: x.created_at, reverse=False
        )

        formatted_messages = []
        for message in sorted_messages:
            iso_time = (
                datetime.fromtimestamp(message.created_at)
                .replace(tzinfo=timezone.utc)
                .isoformat()
            )
            formatted_message = {
                "role": "user" if message.role == "user" else "system",
                "message": message.content[0].text.value,
                "created_at": iso_time,
            }
            formatted_messages.append(formatted_message)

        return jsonify(
            {"message": "Messages retrieved successfully!", "data": formatted_messages}
        )
