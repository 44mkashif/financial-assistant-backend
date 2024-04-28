from datetime import timezone

from constants import ALLOWED_EXTENSIONS

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def format_for_llm(w2_forms):
    """Format W-2 data for use with a language model."""
    data_list = []
    for form in w2_forms:
        data = (
            f"Employer Name: {form.employer.name}\n"
            f"Employer Address: {form.employer.address}\n"
            f"Employer State ID: {form.employer.state_id}\n"
            f"Employer EIN: {form.employer.ein}\n"
            f"Employee Name: {form.employee.name}\n"
            f"Employee SSN: {form.employee.ssn}\n"
            f"Employee Address: {form.employee.address}\n"
            f"Federal Income Tax: {form.tax_information.federal_income_tax}\n"
            f"State Income Tax: {form.tax_information.state_income_tax}\n"
            f"Medicare Tax: {form.tax_information.medicare_tax}\n"
            f"Social Security Tax: {form.tax_information.ss_tax}\n"
            f"Medicare Wages: {form.tax_information.medicare_wages}\n"
            f"Social Security Wages: {form.tax_information.ss_wages}\n"
            f"State Wages and Tips: {form.tax_information.state_wages_tips}"
        )
        data_list.append(data)
    
    return "\n__________\n".join(data_list) if data_list else None


def format(w2_forms):
    return [
        {
            "employer_name": form.employer.name,
            "employer_address": form.employer.address,
            "employer_state_id": form.employer.state_id,
            "employer_ein": form.employer.ein,
            "employee_name": form.employee.name,
            "employee_ssn": form.employee.ssn,
            "employee_address": form.employee.address,
            "federal_income_tax": form.tax_information.federal_income_tax,
            "state_income_tax": form.tax_information.state_income_tax,
            "medicare_tax": form.tax_information.medicare_tax,
            "social_security_tax": form.tax_information.ss_tax,
            "medicare_wages": form.tax_information.medicare_wages,
            "social_security_wages": form.tax_information.ss_wages,
            "state_wages_and_tips": form.tax_information.state_wages_tips,
            "file_name": form.file_name,
            "uploaded_on": form.created_at.replace(tzinfo=timezone.utc).isoformat(),
            "gpt_assistant_id": form.gpt_assistant_id,
            "gpt_thread_id": form.gpt_thread_id,
            "w2_form_id": form.id,
        } for form in w2_forms
    ]
