class StreamCredential:
    def __init__(self, execute_query):
        self.execute_query = execute_query

    @staticmethod
    def create_table(self):
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
        self.execute_query(query)
