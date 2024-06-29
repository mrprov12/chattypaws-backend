from models.user import User
from models.pet import Pet
from models.button import Button
from models.tile import Tile
from models.button_press import ButtonPress
from models.video_stream import VideoStream
from models.session_history import SessionHistory
from models.setting import Setting
from models.notification import Notification
from models.stream_credential import StreamCredential

def create_tables():
    User.create_table()
    Pet.create_table()
    Button.create_table()
    Tile.create_table()
    ButtonPress.create_table()
    VideoStream.create_table()
    SessionHistory.create_table()
    Setting.create_table()
    Notification.create_table()
    StreamCredential.create_table()

if __name__ == "__main__":
    create_tables()
