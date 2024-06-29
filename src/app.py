from dotenv import load_dotenv
from repo.database import init_db

# Load environment variables from .env file
load_dotenv()

if __name__ == "__main__":
   # Init PostgreSQL chattypaws-backend-db 
    init_db()
