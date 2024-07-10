import psycopg2
from app_config import config


def get_db_connection():
    return psycopg2.connect(
        host=config.DB_HOST,
        port=config.DB_PORT,
        database=config.DB_DATABASE_NAME,
        user=config.DB_USERNAME,
        password=config.DB_PASSWORD,
    )


def execute_query(query, params=None):
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(query, params)
            conn.commit()
            if query.strip().lower().startswith("select"):
                return cur.fetchall()
            return None
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()
