from src.app_config import Config

from repo.database import init_db

if __name__ == "__main__":
   # Init PostgreSQL chattypaws-backend-db 
    init_db()
