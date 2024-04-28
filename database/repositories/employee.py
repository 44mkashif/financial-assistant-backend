from database import db
from database.models.employee import Employee


class EmployeeRepository:
    def upsert_employee(self, employee_data, flush=False):
        employee = Employee.query.filter_by(ssn=employee_data["ssn"]).first()
        if not employee:
            employee = Employee(**employee_data)
            db.session.add(employee)
        else:
            for key, value in employee_data.items():
                setattr(employee, key, value)

        if flush:
            db.session.flush()
        else:
            db.session.commit()
        return employee

    def get_employee_by_id(self, employee_id):
        return Employee.query.filter_by(id=employee_id).first()

    def update_employee(self, employee_id, update_data):
        employee = self.get_employee_by_id(employee_id)
        if employee:
            for key, value in update_data.items():
                setattr(employee, key, value)
            db.session.commit()
        return employee

    def delete_employee(self, employee_id):
        employee = self.get_employee_by_id(employee_id)
        if employee:
            db.session.delete(employee)
            db.session.commit()
        return employee
