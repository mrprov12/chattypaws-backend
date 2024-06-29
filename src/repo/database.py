import psycopg2
from src.app_config import config

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

def init_db():
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
    print("Database initialized successfully!")

def get_db_connection():
    conn = psycopg2.connect(
        host=config.DB_HOST,
        port=config.DB_PORT,
        database=config.DB_DATABASE_NAME,
        user=config.DB_USERNAME,
        password=config.DB_PASSWORD
    )
    return conn

def get_credentials(conn, user_id, stream_type):
    with conn.cursor() as cur:
        cur.execute("""
            SELECT url, username, password 
            FROM stream_credentials 
            WHERE user_id = %s AND stream_type = %s
        """, (user_id, stream_type))
        result = cur.fetchone()
        if result:
            return result
        else:
            raise ValueError(f"No credentials found for user_id {user_id} and stream_type {stream_type}")

def execute_query(query, params=None):
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(query, params)
            conn.commit()
            if query.strip().lower().startswith('select'):
                return cur.fetchall()
            return None
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()
