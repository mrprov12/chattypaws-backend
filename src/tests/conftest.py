# tests/conftest.py
import pytest
from src.app import create_app
from src.extensions import db as _db
from src.models import (
    User,
    Pet,
    Button,
    Tile,
    ButtonPress,
    VideoStreams,
    SessionHistory,
    Setting,
    Notification,
    StreamCredential,
    ProcessingResult,
)


@pytest.fixture(scope="session")
def app():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    with app.app_context():
        _db.create_all()
    yield app
    _db.drop_all()


@pytest.fixture(scope="function")
def client(app):
    return app.test_client()


@pytest.fixture(scope="function")
def db(app):
    with app.app_context():
        yield _db
        _db.session.rollback()
        _db.drop_all()
        _db.create_all()
