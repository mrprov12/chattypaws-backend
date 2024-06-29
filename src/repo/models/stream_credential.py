from repo.database import execute_query

class StreamCredential:
    @staticmethod
    def create_table():
        query = """
        CREATE TABLE IF NOT EXISTS stream_credentials (
            id SERIAL PRIMARY KEY,
            user_id INTEGER NOT NULL,
            stream_type VARCHAR(50) NOT NULL, -- 'rtsp' or 'onvif'
            url VARCHAR(255),
            username VARCHAR(255),
            password VARCHAR(255),
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        );
        """
        execute_query(query)
