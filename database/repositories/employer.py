from database import db
from database.models.employer import Employer

class EmployerRepository:
    def upsert_employer(self, employer_data, flush=False):
        employer = Employer.query.filter_by(ein=employer_data['ein']).first()
        if not employer:
            employer = Employer(**employer_data)
            db.session.add(employer)
        else:
            for key, value in employer_data.items():
                setattr(employer, key, value)

        if flush:
            db.session.flush()
        else:
            db.session.commit()
        return employer

    def get_employer_by_id(self, employer_id):
        return Employer.query.filter_by(id=employer_id).first()

    def update_employer(self, employer_id, update_data):
        employer = self.get_employer_by_id(employer_id)
        if employer:
            for key, value in update_data.items():
                setattr(employer, key, value)
            db.session.commit()
        return employer

    def delete_employer(self, employer_id):
        employer = self.get_employer_by_id(employer_id)
        if employer:
            db.session.delete(employer)
            db.session.commit()
        return employer
