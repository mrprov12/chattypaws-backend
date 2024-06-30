import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    def __init__(self):
        self.FLASK_APP = os.environ.get("FLASK_APP")
        self.FLASK_ENV = os.environ.get("FLASK_ENV")
        self.SECRET_KEY = os.environ.get("SECRET_KEY")

        self.DB_HOST = os.getenv("DB_HOST", "0.0.0.0")
        self.DB_PORT = os.getenv("DB_PORT", "5000")
        self.DB_DATABASE_NAME = os.getenv("DB_DATABASE_NAME")
        self.DB_USERNAME = os.getenv("DB_USERNAME")
        self.DB_PASSWORD = os.getenv("DB_PASSWORD")
        self.SCHEMA_FILE = os.getenv("SCHEMA_FILE")

        self.RTSP_URL = os.getenv("RTSP_URL")
        self.STREAM_USERNAME = os.getenv("STREAM_USERNAME")
        self.STREAM_PASSWORD = os.getenv("STREAM_PASSWORD")

        self.ONVIF_IP = os.getenv("ONVIF_IP")
        self.ONVIF_PORT = os.getenv("ONVIF_PORT")
        self.ONVIF_USERNAME = os.getenv("ONVIF_USERNAME")
        self.ONVIF_PASSWORD = os.getenv("ONVIF_PASSWORD")

        self.APP_HOST = os.getenv("APP_HOST", "localhost")
        self.APP_PORT = os.getenv("APP_PORT", "5000")


# Initialize Config object
config = Config()
