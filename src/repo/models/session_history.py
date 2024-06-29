class SessionHistory:
    def __init__(self, execute_query):
        self.execute_query = execute_query

    @staticmethod
    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS session_history (
            session_id SERIAL PRIMARY KEY,
            user_id INTEGER NOT NULL,
            start_time TIMESTAMP NOT NULL,
            end_time TIMESTAMP,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        );
        """
        self.execute_query(query)
