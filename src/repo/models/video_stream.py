from repo.database import execute_query

class ButtonPress:
    @staticmethod
    def create_table():
        query = """
        CREATE TABLE IF NOT EXISTS button_presses (
            press_id SERIAL PRIMARY KEY,
            user_id INTEGER NOT NULL,
            pet_id INTEGER NOT NULL,
            button_id INTEGER NOT NULL,
            timestamp TIMESTAMP NOT NULL,
            confidence FLOAT,
            FOREIGN KEY (user_id) REFERENCES users(user_id),
            FOREIGN KEY (pet_id) REFERENCES pets(pet_id),
            FOREIGN KEY (button_id) REFERENCES buttons(button_id)
        );
        """
        execute_query(query)
