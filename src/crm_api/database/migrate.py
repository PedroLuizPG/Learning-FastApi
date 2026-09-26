from crm_api.database.database import get_connection

CREATE_TASKS_TABLE = """
    CREATE TABLE IF NOT EXISTS tasks(
        id SERIAL PRIMARY KEY,
        title TEXT NOT NULL,
        done  BOOLEAN NOT NULL DEFAULT false,
        created_at TIMESTAMP NOT NULL DEFAULT NOW()
    );
"""

def run_migrations():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(CREATE_TASKS_TABLE)
    conn.commit()
    conn.close()
    print("✔ migrações aplicadas")
    
if __name__ == "__main__":
    run_migrations()
