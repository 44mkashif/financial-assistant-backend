from sqlalchemy.sql import func

from database import db

class User(db.Model):
    __tablename__ = "User"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(
        db.DateTime, server_default=func.now(), onupdate=func.now()
    )
    w2_forms = db.relationship("W2Form", backref="user")
    
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
