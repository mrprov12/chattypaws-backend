# src/routes/init.py
from flask import Flask
from .ping import ping_bp
from .user import user_bp
from .image_processing import image_processing_bp
from .notification import notification_bp
from flask_swagger_ui import get_swaggerui_blueprint


def register_routes(app: Flask):
    app.register_blueprint(ping_bp, url_prefix="/")
    app.register_blueprint(user_bp, url_prefix="/user")
    app.register_blueprint(image_processing_bp, url_prefix="/image_processing")
    app.register_blueprint(notification_bp, url_prefix="/notification")

    SWAGGER_URL = "/swagger"
    API_URL = "/assets/swagger.yaml"
    swaggerui_bp = get_swaggerui_blueprint(
        SWAGGER_URL, API_URL, config={"app_name": "ChattyPaws API"}
    )
    app.register_blueprint(swaggerui_bp, url_prefix=SWAGGER_URL)
