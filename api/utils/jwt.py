from database.repositories.auth_token import AuthTokenRepository


def check_if_token_revoked(jwt_header, jwt_payload):
    auth_token_repo = AuthTokenRepository()
    jti = jwt_payload["jti"]

    return auth_token_repo.is_token_revoked(jti)
