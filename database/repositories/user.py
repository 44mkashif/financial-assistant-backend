from database import db
from database.models.user import User


class UserRepository:
    def add_user(self, user_data, flush=False):
        user = User(**user_data)
        db.session.add(user)
        if flush:
            db.session.flush()
        else:
            db.session.commit()

        return user

    def get_user_by_id(self, user_id):
        return User.query.filter_by(id=user_id).first()

    def get_user_by_email(self, email):
        return User.query.filter_by(email=email).first()
