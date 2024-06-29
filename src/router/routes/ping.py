from flask import Blueprint

ping_bp = Blueprint('ping', __name__)

@ping_bp.route('/')
def index():
    return "Welcome to ChattyPaws Backend API!"

