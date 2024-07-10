# tests/test_db.py
from src.extensions import db
from src.models.user import User
from src.models.pet import Pet
from src.models.button import Button
from src.models.tile import Tile
from src.models.button_press import ButtonPress
from src.models.video_streams import VideoStreams
from src.models.session_history import SessionHistory
from src.models.setting import Setting
from src.models.notification import Notification
from src.models.stream_credential import StreamCredential
from src.models.processing_result import ProcessingResult


def test_user_model(db):
    user = User(username="testuser", password_hash="hash", email="test@example.com")
    db.session.add(user)
    db.session.commit()
    assert user.id is not None


def test_pet_model(db):
    user = User(username="testuser", password_hash="hash", email="test@example.com")
    db.session.add(user)
    db.session.commit()
    pet = Pet(name="testpet", user_id=user.id)
    db.session.add(pet)
    db.session.commit()
    assert pet.id is not None


def test_button_model(db):
    user = User(username="testuser", password_hash="hash", email="test@example.com")
    db.session.add(user)
    db.session.commit()
    tile = Tile(user_id=user.id, name="testtile")
    db.session.add(tile)
    db.session.commit()
    button = Button(name="testbutton", user_id=user.id, tile_id=tile.id)
    db.session.add(button)
    db.session.commit()
    assert button.id is not None


def test_video_stream_model(db):
    user = User(username="testuser", password_hash="hash", email="test@example.com")
    db.session.add(user)
    db.session.commit()
    video_stream = VideoStreams(user_id=user.id, url="http://example.com/stream")
    db.session.add(video_stream)
    db.session.commit()
    assert video_stream.stream_id is not None


def test_notification_model(db):
    user = User(username="testuser", password_hash="hash", email="test@example.com")
    db.session.add(user)
    db.session.commit()
    notification = Notification(user_id=user.id, message="test notification")
    db.session.add(notification)
    db.session.commit()
    assert notification.id is not None


def test_tile_model(db):
    user = User(username="testuser", password_hash="hash", email="test@example.com")
    db.session.add(user)
    db.session.commit()
    tile = Tile(name="testtile", user_id=user.id)
    db.session.add(tile)
    db.session.commit()
    assert tile.id is not None


def test_button_press_model(db):
    user = User(username="testuser", password_hash="hash", email="test@example.com")
    db.session.add(user)
    db.session.commit()
    pet = Pet(name="testpet", user_id=user.id)
    db.session.add(pet)
    db.session.commit()
    button = Button(name="testbutton", user_id=user.id, tile_id=1)
    db.session.add(button)
    db.session.commit()
    button_press = ButtonPress(
        user_id=user.id,
        pet_id=pet.id,
        button_id=button.id,
        timestamp="2024-06-30T12:34:56",
    )
    db.session.add(button_press)
    db.session.commit()
    assert button_press.id is not None


def test_session_history_model(db):
    user = User(username="testuser", password_hash="hash", email="test@example.com")
    db.session.add(user)
    db.session.commit()
    session_history = SessionHistory(user_id=user.id, start_time="2024-06-30T12:34:56")
    db.session.add(session_history)
    db.session.commit()
    assert session_history.id is not None


def test_setting_model(db):
    user = User(username="testuser", password_hash="hash", email="test@example.com")
    db.session.add(user)
    db.session.commit()
    setting = Setting(user_id=user.id, setting_key="theme", setting_value="dark")
    db.session.add(setting)
    db.session.commit()
    assert setting.id is not None


def test_stream_credential_model(db):
    user = User(username="testuser", password_hash="hash", email="test@example.com")
    db.session.add(user)
    db.session.commit()
    stream_credential = StreamCredential(
        user_id=user.id,
        stream_type="rtsp",
        url="http://example.com/stream",
        username="streamuser",
        password="streampass",
    )
    db.session.add(stream_credential)
    db.session.commit()
    assert stream_credential.id is not None


def test_processing_result_model(db):
    processing_result = ProcessingResult(
        timestamp="2024-06-30T12:34:56",
        button_press=True,
        additional_data={"example": "data"},
    )
    db.session.add(processing_result)
    db.session.commit()
    assert processing_result.id is not None
