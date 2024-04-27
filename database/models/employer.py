from sqlalchemy.sql import func

from database import db

class Employer(db.Model):
    __tablename__ = "Employer"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    state_id = db.Column(db.String(50), nullable=True)
    ein = db.Column(db.String(50), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

    w2_forms = db.relationship('W2Form', backref='employer')

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}