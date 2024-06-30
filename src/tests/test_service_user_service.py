# tests/test_services.py

from src.services.user_service import UserService
from src.models import db, User


def test_register_user(db):
    email = "test@example.com"
    password = "securepassword"
    response, status_code = UserService.register_user(email, password)
    assert status_code == 201
    assert response["message"] == "User registered successfully"
    assert "user_id" in response


def test_login_user(db):
    email = "test@example.com"
    password = "securepassword"
    user = User(email=email, password_hash=password)
    db.session.add(user)
    db.session.commit()

    response, status_code = UserService.login_user(email, password)
    assert status_code == 200
    assert response["message"] == "Login successful"


def test_get_current_user(db):
    user = User(username="testuser", password_hash="hash", email="test@example.com")
    db.session.add(user)
    db.session.commit()
    current_user = UserService.get_current_user()
    assert current_user is not None
    assert current_user.email == "test@example.com"
