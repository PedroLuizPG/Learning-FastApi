import psycopg2.extras
from datetime import datetime
from crm_api.database.database import get_connection
from .entities import Task
from .schemas import TaskCreate,TaskUpdate

def _row_to_task(row: dict) -> Task:
    return Task(
        id=row["id"],
        title=row["title"],
        done=row["done"],
        created_at=row["created_at"]
    )
    
class PostgresRepository:
    """Implementa TaskRepository (repository.py) usando psycopg2/postgreSQL."""
    
    def findAll(self) -> list[Task]:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks ORDER BY id DESC")
        rows = cursor.fetchall()
        conn.close()
        return [_row_to_task(row) for row in rows]
    
    def findById(self,id:int) -> Task | None:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
                SELECT * FROM tasks WHERE id = %s
            """,
            (id,)
        )
        row = cursor.fetchone()
        conn.close()
        
        return _row_to_task(row) if row else None
    
    def create(self, data: TaskCreate) -> Task:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tasks (title) VALUES (%s) RETURNING *",
            (data.title,),
        )
        row = cursor.fetchone()
        conn.commit()
        conn.close()
        
        return _row_to_task(row)
    
    def update(self, data:TaskUpdate, id:int) -> Task | None:
        current = self.findById(id)
        if not current:
            return None
        
        title = data.title if data.title is not None else current.title
        done = data.done if data.done is not None else current.done
        
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
                UPDATE tasks SET title = %s, done = %s 
                WHERE id = %s            
            """, (title,done,id,)
        )
        conn.commit()
        conn.close()
        
        return self.findById(id)
    
    def delete(self, id: int) -> bool:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = %s", (id,))
        conn.commit()
        conn.close()
        return cursor.rowcount > 0