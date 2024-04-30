from database import db
from database.models.auth_token import AuthToken


class AuthTokenRepository:
    def add_revoked_token(self, jti, user_id, type):
        revoked_token = AuthToken(
            jti=jti, is_revoked=True, user_id=user_id, type=type
        )
        db.session.add(revoked_token)
        db.session.commit()

    def is_token_revoked(self, jti):
        return (
            AuthToken.query.filter_by(jti=jti, is_revoked=True).first()
            is not None
        )
