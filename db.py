import sqlite3
import os

# Absolute path for DB
DB_PATH = os.path.join(os.path.dirname(__file__), "project.db")

def create_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    # Users table
    c.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL,
        created_at TEXT
    )
    """)
    # Files table
    c.execute("""
    CREATE TABLE IF NOT EXISTS files(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sender_id INTEGER,
        receiver_id INTEGER,
        file_name TEXT,
        file_path TEXT,
        encryption_key TEXT,
        transfer_method TEXT,
        status TEXT,
        hash_value TEXT,
        timestamp TEXT
    )
    """)
    # Logs table
    c.execute("""
    CREATE TABLE IF NOT EXISTS logs(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        action TEXT,
        file_id INTEGER,
        device_info TEXT,
        timestamp TEXT
    )
    """)
    conn.commit()
    conn.close()
    print(f"Database created or verified at: {DB_PATH}")

if __name__ == "__main__":
    create_db()






