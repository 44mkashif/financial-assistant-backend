from sqlalchemy.sql import func

from database import db

class Employee(db.Model):
    __tablename__ = "Employee"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    ssn = db.Column(db.String(11), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

    w2_forms = db.relationship('W2Form', backref='employee')

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
