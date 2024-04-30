from flask import current_app
from flask_jwt_extended import jwt_required

from api.auth import auth_bp
from api.auth.auth import Auth


class AuthRoutes:
    @staticmethod
    def get_auth_instance():
        if not hasattr(current_app, "auth_instance"):
            current_app.auth_instance = Auth()
        return current_app.auth_instance

    @auth_bp.route("/signup", methods=["POST"])
    def signup():
        auth = AuthRoutes.get_auth_instance()
        return auth.signup()

    @auth_bp.route("/login", methods=["POST"])
    def login():
        auth = AuthRoutes.get_auth_instance()
        return auth.login()

    @auth_bp.route("/logout", methods=["POST"])
    @jwt_required()
    def logout():
        auth = AuthRoutes.get_auth_instance()
        return auth.logout()
