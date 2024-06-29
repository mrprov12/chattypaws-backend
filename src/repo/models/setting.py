class Setting:
    def __init__(self, execute_query):
        self.execute_query = execute_query

    @staticmethod
    def create_table(self):
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
        self.execute_query(query)
