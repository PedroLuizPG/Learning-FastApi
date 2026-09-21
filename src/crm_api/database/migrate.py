from crm_api.database.database import get_connection

CREATE_TASKS_TABLE = """
    CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        done  INTEGER NOT NULL DEFAULT 0,
        created_at TEXT NOT NULL DEFAULT (datetime('now'))
    );
"""

def run_migrations():
    conn = get_connection()
    conn.execute(CREATE_TASKS_TABLE)
    conn.commit()
    conn.close()
    print("✔ migrações aplicadas")
    
if __name__ == "__main__":
    run_migrations()
