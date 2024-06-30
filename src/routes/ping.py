# src/routes/ping.py
from flask import Blueprint, jsonify

ping_bp = Blueprint("ping", __name__)


@ping_bp.route("/")
def index():
    return jsonify({"message": "Welcome to ChattyPaws Backend API!"}), 200
