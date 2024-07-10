# app.py
from flask import Flask
from app_config import Config
from extensions import db, migrate, cors
from routes.init import register_routes


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.secret_key = app.config["SECRET_KEY"]

    # Enable CORS
    cors.init_app(app)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register routes
    register_routes(app)

    setup_error_handlers(app)
    setup_logging(app)

    return app


def setup_error_handlers(app):
    @app.errorhandler(404)
    def not_found(error):
        return {"error": "Not Found"}, 404

    @app.errorhandler(500)
    def internal_error(error):
        app.logger.error(f"Server Error: {error}")
        return {"error": "Internal Server Error"}, 500


def setup_logging(app):
    import logging

    logging.basicConfig(level=logging.INFO)
    app.logger.info("Logging setup complete.")


if __name__ == "__main__":
    app = create_app()
    app.run(
        host=app.config["APP_HOST"],
        port=int(app.config["APP_PORT"]),
        debug=app.config["FLASK_ENV"] == "development",
    )
