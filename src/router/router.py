from flask import Blueprint
from .routes.ping import ping_bp
from .routes.user import user_bp
from .routes.image_processing import image_processing_bp
from .routes.notification import notification_bp


class Router:
    def __init__(self):
        self.router_bp = Blueprint("router", __name__)

    def setup_routes(self):
        # Register blueprints
        self.router_bp.register_blueprint(ping_bp)
        self.router_bp.register_blueprint(user_bp)
        self.router_bp.register_blueprint(image_processing_bp)
        self.router_bp.register_blueprint(notification_bp)
        # Register Swagger UI blueprint
        from flask_swagger_ui import get_swaggerui_blueprint

        SWAGGER_URL = "/swagger"
        API_URL = "/assets/swagger.yaml"
        swaggerui_bp = get_swaggerui_blueprint(
            SWAGGER_URL, API_URL, config={"app_name": "ChattyPaws API"}
        )
        self.router_bp.register_blueprint(swaggerui_bp, url_prefix=SWAGGER_URL)


router = Router()
