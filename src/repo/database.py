import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USERNAME"),
        password=os.getenv("DB_PASSWORD")
    )
    return conn

def get_credentials(conn, user_id, stream_type):
    with conn.cursor() as cur:
        cur.execute("""
            SELECT url, username, password 
            FROM stream_credentials 
            WHERE user_id = %s AND stream_type = %s
        """, (user_id, stream_type))
        result = cur.fetchone()
        if result:
            return result
        else:
            raise ValueError(f"No credentials found for user_id {user_id} and stream_type {stream_type}")

def execute_query(query, params=None):
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(query, params)
            conn.commit()
            return cur.fetchall()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()