import traceback
from flask import jsonify
from functools import wraps
from werkzeug.exceptions import BadRequest

def handle_api_errors(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except BadRequest as e:
            traceback.print_exc()
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            print(f"An error occurred: {type(e).__name__} - {str(e)}")
            traceback.print_exc()
            return (
                jsonify(
                    {"error": "An error occurred while processing the request"}
                ),
                500,
            )

    return decorated_function
