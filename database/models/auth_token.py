import uuid
from sqlalchemy.sql import func
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from database import db


class AuthToken(db.Model):
    __tablename__ = "AuthToken"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey("User.id"), nullable=False)
    jti = db.Column(
        UUID(as_uuid=True),
        default=uuid.uuid4,
        nullable=False,
        unique=True,
        index=True,
    )
    type = db.Column(db.String(20), nullable=False)
    is_revoked = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(
        db.DateTime, server_default=func.now(), onupdate=func.now()
    )

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
