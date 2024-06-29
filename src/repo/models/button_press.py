class ButtonPress:
    def __init__(self, execute_query):
        self.execute_query = execute_query

    @staticmethod
    def create_table(self):
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
        self.execute_query(query)
