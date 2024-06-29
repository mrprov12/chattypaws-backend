from repo.database import execute_query

class SessionHistory:
    @staticmethod
    def create_table():
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
        execute_query(query)
