from flask import Blueprint
from ..route_handlers.user_handler import UserHandler

user_bp = Blueprint('user', __name__)
user_handler = UserHandler()

@user_bp.route('/user/login', methods=['POST'])
def user_login():
    return user_handler.login()

@user_bp.route('/user/register', methods=['POST'])
def user_register():
    return user_handler.register()

@user_bp.route('/user', methods=['GET'])
def user_get_current_user():
    return user_handler.get_current_user()
