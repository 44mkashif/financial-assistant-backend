from sqlalchemy.sql import func
from sqlalchemy import ForeignKey

from database import db

class TaxInformation(db.Model):
    __tablename__ = "TaxInformation"

    id = db.Column(db.Integer, primary_key=True)
    w2_form_id = db.Column(db.Integer, ForeignKey('W2Form.id'), nullable=False)
    federal_income_tax = db.Column(db.Float, nullable=True)
    state_income_tax = db.Column(db.Float, nullable=True)
    medicare_tax = db.Column(db.Float, nullable=True)
    ss_tax = db.Column(db.Float, nullable=True)
    medicare_wages = db.Column(db.Float, nullable=True)
    ss_wages = db.Column(db.Float, nullable=True)
    state_wages_tips = db.Column(db.Float, nullable=True)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
