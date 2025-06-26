import os
import pymysql
from dotenv import load_dotenv
def get_db_connection():
    return pymysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        port=3306,
        connect_timeout=5,
        cursorclass=pymysql.cursors.DictCursor
    )

load_dotenv()

def log_ai_interaction(username, module, input_text, ai_response):
    try:
        conn = pymysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
        )
        with conn.cursor() as cursor:
            sql = """
                INSERT INTO ai_logs (username, module, input_text, ai_response)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(sql, (username, module, input_text, ai_response))
        conn.commit()
        conn.close()
    except Exception as e:
        print("❌ Logging failed:", e)


