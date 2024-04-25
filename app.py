from flask import Flask
from flask_cors import CORS

from config import Config

from api.auth import auth_bp
from chatbot import chatbot_bp
from langchain import langchain_bp

class App(Flask):
    def __init__(self, *args, **kwargs):
        super(App, self).__init__(*args, **kwargs)
        self.config.from_object(Config)

    def register_blueprints(self):
        self.register_blueprint(auth_bp)
        self.register_blueprint(chatbot_bp)
        self.register_blueprint(langchain_bp)
        

app = App(__name__)
CORS(app)

app.register_blueprints()

if __name__ == "__main__":
    app.run(debug=True)
