from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate

from config import Config
from database import db
from database.models import *
from constants import MIGRATION_DIR

from api.auth import auth_bp
from chatbot import chatbot_bp
from langchain import langchain_bp
from api.w2_form import w2_form_bp

migrate = Migrate()

class App(Flask):
    def __init__(self, *args, **kwargs):
        super(App, self).__init__(*args, **kwargs)
        self.config.from_object(Config)

        db.init_app(self)
        migrate.init_app(self, db, directory=MIGRATION_DIR)

    def register_blueprints(self):
        self.register_blueprint(chatbot_bp)
        self.register_blueprint(langchain_bp)
        self.register_blueprint(auth_bp, url_prefix='/api/v1/auth')
        self.register_blueprint(w2_form_bp, url_prefix='/api/v1/w2_form')

app = App(__name__)
CORS(app)

app.register_blueprints()

if __name__ == "__main__":
    app.run(debug=True)
