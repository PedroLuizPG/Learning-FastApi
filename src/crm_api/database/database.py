import sqlite3
from crm_api.config.config import settings

DB_PATH = settings.DATABASE_URL.replace("sqlite:///", "")

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    
    return conn