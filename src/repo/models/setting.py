from repo.database import execute_query

class Setting:
    @staticmethod
    def create_table():
        query = """
        CREATE TABLE IF NOT EXISTS settings (
            setting_id SERIAL PRIMARY KEY,
            user_id INTEGER NOT NULL,
            setting_key VARCHAR(255) NOT NULL,
            setting_value TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        );
        """
        execute_query(query)
