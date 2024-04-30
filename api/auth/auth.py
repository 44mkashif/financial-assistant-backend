import traceback
from flask import request, jsonify
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import get_jwt, get_jwt_identity, create_access_token

from config import Config
from database.repositories.user import UserRepository
from api.utils.handle_api_errors import handle_api_errors
from api.auth.validations import SignupSchema, LoginSchema
from database.repositories.auth_token import AuthTokenRepository

class Auth:
    def __init__(self):
        self.user_repo = UserRepository()
        self.auth_token_repo = AuthTokenRepository()

    @handle_api_errors
    def signup(self):
        try:
            data = SignupSchema(**request.json)

            existing_user = self.user_repo.get_user_by_email(data.email)
            if existing_user:
                return jsonify({"error": "Email already exists!"}), 400

            user = self.user_repo.add_user(
                {
                    "name": data.name,
                    "email": data.email,
                    "password": generate_password_hash(data.password),
                }
            )

            token = create_access_token(
                        identity=user.id,
                        expires_delta=Config.JWT_ACCESS_TOKEN_EXPIRES,
                    )

            response_data = {
                "user_id": user.id,
                "email": user.email,
                "name": user.name,
                "access_token": token
            }
            return (
                jsonify(
                    {
                        "message": "User registered successfully",
                        "data": response_data,
                    }
                ),
                200,
            )
        except SQLAlchemyError as e:
            print(
                f"An SQLAlchemyError occurred: {type(e).__name__} - {str(e)}"
            )
            traceback.print_exc()
            return jsonify({"error": "Database error occurred!"}), 500

    @handle_api_errors
    def login(self):
        data = LoginSchema(**request.json)

        user = self.user_repo.get_user_by_email(data.email)

        if user:
            if check_password_hash(user.password, data.password):
                response_data = {
                    "user_id": user.id,
                    "access_token": create_access_token(
                        identity=user.id,
                        expires_delta=Config.JWT_ACCESS_TOKEN_EXPIRES,
                    )
                }
                return (
                    jsonify(
                        {"message": "Login successful", "data": response_data}
                    ),
                    200,
                )

        return jsonify({"error": "Incorrect email or password!"}), 401

    @handle_api_errors
    def logout(self):
        user_id = get_jwt_identity()
        access_token_jti = get_jwt()["jti"]

        self.auth_token_repo.add_revoked_token(
            access_token_jti, user_id, "access"
        )

        return jsonify({"message": "Access token has been revoked"}), 200
