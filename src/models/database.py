import psycopg2
from app_config import config
from .models.user import User
from .models.pet import Pet
from .models.button import Button
from .models.tile import Tile
from .models.button_press import ButtonPress
from .models.video_streams import VideoStreams
from .models.session_history import SessionHistory
from .models.setting import Setting
from .models.notification import Notification
from .models.stream_credential import StreamCredential


class Repo:
    def __init__(self):
        self.conn = self.get_db_connection()

        self.ButtonPress = ButtonPress(self.execute_query)
        self.Button = Button(self.execute_query)
        self.Notification = Notification(self.execute_query)
        self.Pet = Pet(self.execute_query)
        self.SessionHistory = SessionHistory(self.execute_query)
        self.Setting = Setting(self.execute_query)
        self.StreamCredential = StreamCredential(self.execute_query)
        self.Tile = Tile(self.execute_query)
        self.User = User(self.execute_query)
        self.VideoStreams = VideoStreams(self.execute_query)

    def create_tables(self):
        self.ButtonPress.create_table()
        self.Button.create_table()
        self.Notification.create_table()
        self.Pet.create_table()
        self.SessionHistory.create_table()
        self.Setting.create_table()
        self.StreamCredential.create_table()
        self.Tile.create_table()
        self.User.create_table()
        self.VideoStream.create_table()
        print("Database initialized successfully!")

    def get_db_connection(self):
        conn = psycopg2.connect(
            host=config.DB_HOST,
            port=config.DB_PORT,
            database=config.DB_DATABASE_NAME,
            user=config.DB_USERNAME,
            password=config.DB_PASSWORD,
        )
        return conn

    def get_credentials(self, user_id, stream_type):
        with self.conn.cursor() as cur:
            cur.execute(
                """
                SELECT url, username, password 
                FROM stream_credentials 
                WHERE user_id = %s AND stream_type = %s
            """,
                (user_id, stream_type),
            )
            result = cur.fetchone()
            if result:
                return result
            else:
                raise ValueError(
                    f"No credentials found for user_id {user_id} and stream_type {stream_type}"
                )

    def execute_query(self, query, params=None):
        try:
            with self.conn.cursor() as cur:
                cur.execute(query, params)
                self.conn.commit()
                if query.strip().lower().startswith("select"):
                    return cur.fetchall()
                return None
        except Exception as e:
            self.conn.rollback()
            raise e
        finally:
            self.conn.close()


# Example of using the Repo class
repo = Repo()
