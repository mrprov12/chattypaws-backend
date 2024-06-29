class Button:
    def __init__(self, execute_query):
        self.execute_query = execute_query

    @staticmethod
    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS buttons (
            button_id SERIAL PRIMARY KEY,
            user_id INTEGER NOT NULL,
            pet_id INTEGER,
            tile_id INTEGER NOT NULL,
            name VARCHAR(255) NOT NULL,
            position_x INTEGER,
            position_y INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(user_id),
            FOREIGN KEY (pet_id) REFERENCES pets(pet_id),
            FOREIGN KEY (tile_id) REFERENCES tiles(tile_id)
        );
        """
        self.execute_query(query)
