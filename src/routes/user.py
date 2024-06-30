# routes/user.py
from flask import Blueprint, request, jsonify
from ..services.user_service import UserService

user_bp = Blueprint("user", __name__)


@user_bp.route("/login", methods=["POST"])
def user_login():
    data = request.json
    email = data.get("email")
    password = data.get("password")
    return jsonify(UserService.login_user(email, password))


@user_bp.route("/register", methods=["POST"])
def user_register():
    data = request.json
    email = data.get("email")
    password = data.get("password")
    return jsonify(UserService.register_user(email, password))


@user_bp.route("/", methods=["GET"])
def user_get_current_user():
    return jsonify(UserService.get_current_user())
