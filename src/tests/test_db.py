import unittest
from repo.database import execute_query
from repo.models.user import User
from repo.models.pet import Pet
from repo.models.button import Button
from repo.models.tile import Tile
from repo.models.button_press import ButtonPress
from repo.models.video_stream import VideoStream
from repo.models.session_history import SessionHistory
from repo.models.setting import Setting
from repo.models.notification import Notification
from repo.models.stream_credential import StreamCredential

class TestDatabase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create tables
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

    def test_user_table(self):
        query = "INSERT INTO users (username, password_hash, email) VALUES (%s, %s, %s) RETURNING user_id;"
        params = ('test_user', 'hash123', 'test@example.com')
        user_id = execute_query(query, params)[0][0]
        
        query = "SELECT * FROM users WHERE user_id = %s;"
        params = (user_id,)
        user = execute_query(query, params)[0]
        
        self.assertEqual(user[1], 'test_user')
        self.assertEqual(user[2], 'hash123')
        self.assertEqual(user[3], 'test@example.com')

    def test_pet_table(self):
        query = "INSERT INTO users (username, password_hash) VALUES (%s, %s) RETURNING user_id;"
        user_params = ('pet_owner', 'hash123')
        user_id = execute_query(query, user_params)[0][0]

        query = "INSERT INTO pets (user_id, name, breed, sex, photo_url) VALUES (%s, %s, %s, %s, %s) RETURNING pet_id;"
        params = (user_id, 'Buddy', 'Golden Retriever', 'Male', 'http://example.com/buddy.jpg')
        pet_id = execute_query(query, params)[0][0]

        query = "SELECT * FROM pets WHERE pet_id = %s;"
        params = (pet_id,)
        pet = execute_query(query, params)[0]

        self.assertEqual(pet[1], user_id)
        self.assertEqual(pet[2], 'Buddy')
        self.assertEqual(pet[3], 'Golden Retriever')
        self.assertEqual(pet[4], 'Male')
        self.assertEqual(pet[5], 'http://example.com/buddy.jpg')

    def test_button_table(self):
        query = "INSERT INTO users (username, password_hash) VALUES (%s, %s) RETURNING user_id;"
        user_params = ('button_user', 'hash123')
        user_id = execute_query(query, user_params)[0][0]

        query = "INSERT INTO tiles (user_id, name) VALUES (%s, %s) RETURNING tile_id;"
        tile_params = (user_id, 'Living Room')
        tile_id = execute_query(query, tile_params)[0][0]

        query = "INSERT INTO buttons (user_id, tile_id, name, position_x, position_y) VALUES (%s, %s, %s, %s, %s) RETURNING button_id;"
        params = (user_id, tile_id, 'Play', 1, 1)
        button_id = execute_query(query, params)[0][0]

        query = "SELECT * FROM buttons WHERE button_id = %s;"
        params = (button_id,)
        button = execute_query(query, params)[0]

        self.assertEqual(button[1], user_id)
        self.assertEqual(button[3], tile_id)
        self.assertEqual(button[4], 'Play')
        self.assertEqual(button[5], 1)
        self.assertEqual(button[6], 1)

    def test_tile_table(self):
        query = "INSERT INTO users (username, password_hash) VALUES (%s, %s) RETURNING user_id;"
        user_params = ('tile_user', 'hash123')
        user_id = execute_query(query, user_params)[0][0]

        query = "INSERT INTO tiles (user_id, name) VALUES (%s, %s) RETURNING tile_id;"
        params = (user_id, 'Bedroom')
        tile_id = execute_query(query, params)[0][0]

        query = "SELECT * FROM tiles WHERE tile_id = %s;"
        params = (tile_id,)
        tile = execute_query(query, params)[0]

        self.assertEqual(tile[1], user_id)
        self.assertEqual(tile[2], 'Bedroom')

    def test_button_press_table(self):
        query = "INSERT INTO users (username, password_hash) VALUES (%s, %s) RETURNING user_id;"
        user_params = ('press_user', 'hash123')
        user_id = execute_query(query, user_params)[0][0]

        query = "INSERT INTO pets (user_id, name) VALUES (%s, %s) RETURNING pet_id;"
        pet_params = (user_id, 'Rex')
        pet_id = execute_query(query, pet_params)[0][0]

        query = "INSERT INTO tiles (user_id, name) VALUES (%s, %s) RETURNING tile_id;"
        tile_params = (user_id, 'Kitchen')
        tile_id = execute_query(query, tile_params)[0][0]

        query = "INSERT INTO buttons (user_id, tile_id, name, position_x, position_y) VALUES (%s, %s, %s, %s, %s) RETURNING button_id;"
        button_params = (user_id, tile_id, 'Eat', 2, 3)
        button_id = execute_query(query, button_params)[0][0]

        query = "INSERT INTO button_presses (user_id, pet_id, button_id, timestamp, confidence) VALUES (%s, %s, %s, NOW(), %s) RETURNING press_id;"
        params = (user_id, pet_id, button_id, 0.95)
        press_id = execute_query(query, params)[0][0]

        query = "SELECT * FROM button_presses WHERE press_id = %s;"
        params = (press_id,)
        press = execute_query(query, params)[0]

        self.assertEqual(press[1], user_id)
        self.assertEqual(press[2], pet_id)
        self.assertEqual(press[3], button_id)
        self.assertAlmostEqual(press[5], 0.95, places=2)

    def test_video_stream_table(self):
        query = "INSERT INTO users (username, password_hash) VALUES (%s, %s) RETURNING user_id;"
        user_params = ('stream_user', 'hash123')
        user_id = execute_query(query, user_params)[0][0]

        query = "INSERT INTO video_streams (user_id, url) VALUES (%s, %s) RETURNING stream_id;"
        params = (user_id, 'http://example.com/stream')
        stream_id = execute_query(query, params)[0][0]

        query = "SELECT * FROM video_streams WHERE stream_id = %s;"
        params = (stream_id,)
        stream = execute_query(query, params)[0]

        self.assertEqual(stream[1], user_id)
        self.assertEqual(stream[2], 'http://example.com/stream')

    def test_session_history_table(self):
        query = "INSERT INTO users (username, password_hash) VALUES (%s, %s) RETURNING user_id;"
        user_params = ('session_user', 'hash123')
        user_id = execute_query(query, user_params)[0][0]

        query = "INSERT INTO session_history (user_id, start_time, end_time) VALUES (%s, NOW(), NOW()) RETURNING session_id;"
        params = (user_id,)
        session_id = execute_query(query, params)[0][0]

        query = "SELECT * FROM session_history WHERE session_id = %s;"
        params = (session_id,)
        session = execute_query(query, params)[0]

        self.assertEqual(session[1], user_id)

    def test_setting_table(self):
        query = "INSERT INTO users (username, password_hash) VALUES (%s, %s) RETURNING user_id;"
        user_params = ('setting_user', 'hash123')
        user_id = execute_query(query, user_params)[0][0]

        query = "INSERT INTO settings (user_id, setting_key, setting_value) VALUES (%s, %s, %s) RETURNING setting_id;"
        params = (user_id, 'theme', 'dark')
        setting_id = execute_query(query, params)[0][0]

        query = "SELECT * FROM settings WHERE setting_id = %s;"
        params = (setting_id,)
        setting = execute_query(query, params)[0]

        self.assertEqual(setting[1], user_id)
        self.assertEqual(setting[2], 'theme')
        self.assertEqual(setting[3], 'dark')

    def test_notification_table(self):
        query = "INSERT INTO users (username, password_hash) VALUES (%s, %s) RETURNING user_id;"
        user_params = ('notify_user', 'hash123')
        user_id = execute_query(query, user_params)[0][0]

        query = "INSERT INTO notifications (user_id, message, type, read) VALUES (%s, %s, %s, %s) RETURNING notification_id;"
        params = (user_id, 'You have a new message!', 'info', False)
        notification_id = execute_query(query, params)[0][0]

        query = "SELECT * FROM notifications WHERE notification_id = %s;"
        params = (notification_id,)
        notification = execute_query(query, params)[0]

        self.assertEqual(notification[1], user_id)
        self.assertEqual(notification[2], 'You have a new message!')
        self.assertEqual(notification[3], 'info')
        self.assertFalse(notification[4])

    def test_stream_credential_table(self):
        query = "INSERT INTO users (username, password_hash) VALUES (%s, %s) RETURNING user_id;"
        user_params = ('stream_user', 'hash123')
        user_id = execute_query(query, user_params)[0][0]

        query = "INSERT INTO stream_credentials (user_id, stream_type, url, username, password) VALUES (%s, %s, %s, %s, %s) RETURNING id;"
        params = (user_id, 'rtsp', 'rtsp://example.com/stream', 'stream_user', 'stream_pass')
        credential_id = execute_query(query, params)[0][0]

        query = "SELECT * FROM stream_credentials WHERE id = %s;"
        params = (credential_id,)
        credential = execute_query(query, params)[0]

        self.assertEqual(credential[1], user_id)
        self.assertEqual(credential[2], 'rtsp')
        self.assertEqual(credential[3], 'rtsp://example.com/stream')
        self.assertEqual(credential[4], 'stream_user')
        self.assertEqual(credential[5], 'stream_pass')

if __name__ == '__main__':
    unittest.main()
