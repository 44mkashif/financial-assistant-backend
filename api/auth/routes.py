from flask import current_app
from api.auth import auth_bp
from api.auth.auth import Auth


class AuthRoutes:
    @staticmethod
    def get_auth_instance():
        if not hasattr(current_app, "auth_instance"):
            current_app.auth_instance = Auth()
        return current_app.auth_instance

    @auth_bp.route("hello", methods=["GET"])
    def hello():
        auth = AuthRoutes.get_auth_instance()
        response = auth.hello()
        return response
