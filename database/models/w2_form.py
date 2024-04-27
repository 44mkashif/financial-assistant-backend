from sqlalchemy.sql import func
from sqlalchemy import ForeignKey

from database import db

class W2Form(db.Model):
    __tablename__ = "W2Form"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey("User.id"), nullable=False)
    employer_id = db.Column(db.Integer, ForeignKey("Employer.id"), nullable=False)
    employee_id = db.Column(db.Integer, ForeignKey("Employee.id"), nullable=False)
    file_name = db.Column(db.String(255), nullable=False)
    file_path = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    tax_information = db.relationship("TaxInformation", backref="w2_form", uselist=False)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
