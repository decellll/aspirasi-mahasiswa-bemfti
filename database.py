import mysql.connector
from config import DB_CONFIG

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

def create_aspiration(kategori, pesan):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = "INSERT INTO aspirasi (kategori, pesan) VALUES (%s, %s)"
        cursor.execute(query, (kategori, pesan))
        conn.commit()
    except mysql.connector.Error as err:
        conn.rollback()
        raise err
    finally:
        cursor.close()
        conn.close()
