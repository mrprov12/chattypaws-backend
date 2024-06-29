from repo.database import execute_query

class Pet:
    @staticmethod
    def create_table():
        query = """
        CREATE TABLE IF NOT EXISTS pets (
            pet_id SERIAL PRIMARY KEY,
            user_id INTEGER NOT NULL,
            name VARCHAR(255) NOT NULL,
            breed VARCHAR(255),
            sex VARCHAR(10),
            photo_url TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        );
        """
        execute_query(query)
