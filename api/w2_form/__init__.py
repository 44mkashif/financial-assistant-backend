from flask import Blueprint

w2_form_bp = Blueprint("w2_form", __name__)

from . import routes
