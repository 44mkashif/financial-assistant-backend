from flask import current_app
from flask_jwt_extended import jwt_required

from api.w2_form import w2_form_bp
from api.w2_form.w2_form import W2Form


class W2FormRoutes:
    @staticmethod
    def get_w2_form_instance():
        if not hasattr(current_app, "w2_form_instance"):
            current_app.w2_form_instance = W2Form()
        return current_app.w2_form_instance

    @w2_form_bp.route("/upload", methods=["POST"])
    @jwt_required()
    def upload():
        w2_form = W2FormRoutes.get_w2_form_instance()
        return w2_form.upload()

    @w2_form_bp.route("/list", methods=["GET"])
    @jwt_required()
    def fetch_w2_data_for_user():
        w2_form = W2FormRoutes.get_w2_form_instance()
        return w2_form.fetch_w2_data_for_user()
