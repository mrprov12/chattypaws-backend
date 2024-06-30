from flask import Flask
from flask_cors import CORS
import logging
from app_config import config
from repo.database import repo
from router.router import router


class App:
    def __init__(self):
        self.config = config
        self.app = Flask(__name__, static_folder="assets")
        self.app.config.from_object(config)
        self.app.secret_key = self.config.SECRET_KEY

        # Enable CORS
        CORS(self.app)

        # Initialize repository and router
        self.repo = repo
        self.router = router

        self.setup_routes()
        self.setup_error_handlers()
        self.setup_logging()

    def setup_routes(self):
        try:
            self.router.setup_routes()
            self.app.register_blueprint(self.router.router_bp)
        except Exception as e:
            self.app.logger.error(f"Error setting up routes: {e}")
            raise

    def setup_error_handlers(self):
        @self.app.errorhandler(404)
        def not_found(error):
            return {"error": "Not Found"}, 404

        @self.app.errorhandler(500)
        def internal_error(error):
            self.app.logger.error(f"Server Error: {error}")
            return {"error": "Internal Server Error"}, 500

    def setup_logging(self):
        logging.basicConfig(level=logging.INFO)
        self.app.logger.info("Logging setup complete.")

    def run(self):
        try:
            self.app.run(
                host=self.config.APP_HOST,
                port=int(self.config.APP_PORT),
                debug=self.config.FLASK_ENV == "development",
            )
        except Exception as e:
            self.app.logger.error(f"Error running the application: {e}")
            raise

    def close(self):
        try:
            self.repo.close()
        except Exception as e:
            self.app.logger.error(f"Error closing the repository: {e}")
            raise


if __name__ == "__main__":
    app_instance = App()
    try:
        app_instance.run()
    finally:
        app_instance.close()
