from flask import current_app
from flask_jwt_extended import jwt_required

from api.chat import chat_bp
from api.chat.chat import Chat


class ChatRoutes:
    @staticmethod
    def get_chat_instance():
        if not hasattr(current_app, "chat_instance"):
            current_app.chat_instance = Chat()
        return current_app.chat_instance

    @chat_bp.route("/question", methods=["POST"])
    @jwt_required()
    def question():
        chat = ChatRoutes.get_chat_instance()
        return chat.question()

    @chat_bp.route("/messages/<gpt_thread_id>", methods=["GET"])
    @jwt_required()
    def get_messages(gpt_thread_id):
        chat = ChatRoutes.get_chat_instance()
        return chat.get_messages(gpt_thread_id)
