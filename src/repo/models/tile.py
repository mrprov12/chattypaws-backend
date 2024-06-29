from repo.database import execute_query

class Tile:
    @staticmethod
    def create_table():
        query = """
        CREATE TABLE IF NOT EXISTS tiles (
            tile_id SERIAL PRIMARY KEY,
            user_id INTEGER NOT NULL,
            name VARCHAR(255),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        );
        """
        execute_query(query)
