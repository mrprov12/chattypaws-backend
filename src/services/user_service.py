# services/user_service.py
from ..models import db, User


class UserService:
    @staticmethod
    def register_user(email, password):
        try:
            new_user = User(email=email, password_hash=password)
            db.session.add(new_user)
            db.session.commit()
            return {
                "message": "User registered successfully",
                "user_id": new_user.id,
            }, 201
        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}, 400

    @staticmethod
    def login_user(email, password):
        # Implement the logic to verify username and password
        return {"message": "Login successful"}, 200

    @staticmethod
    def get_current_user():
        # Implement the logic to get current user
        return {"user": "Current user details"}, 200
