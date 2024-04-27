from flask import current_app
from api.w2_form import w2_form_bp
from api.w2_form.w2_form import W2Form


class W2FormRoutes:
    @staticmethod
    def get_w2_form_instance():
        if not hasattr(current_app, "w2_form_instance"):
            current_app.w2_form_instance = W2Form()
        return current_app.w2_form_instance

    @w2_form_bp.route("/upload", methods=["POST"])
    def upload():
        w2_form = W2FormRoutes.get_w2_form_instance()
        return w2_form.upload()

