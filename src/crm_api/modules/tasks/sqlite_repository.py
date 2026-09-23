import sqlite3
from datetime import datetime
from crm_api.database.database import get_connection
from .entities import Task
from .schemas import TaskCreate,TaskUpdate

def _row_to_task(row: sqlite3.Row) -> Task:
    return Task(
        id=row["id"],
        title=row["title"],
        done=bool(row["done"]),
        created_at=datetime.fromisoformat(row["created_at"])
    )
    
class SqliteRepository:
    """Implementa TaskRepository (repository.py) usando sqlite3."""
    
    def findAll(self) -> list[Task]:
        conn = get_connection()
        rows = conn.execute("SELECT * FROM tasks ORDER BY id DESC").fetchall()
        conn.close()
        return [_row_to_task(row) for row in rows]
    
    def findById(self,id:int) -> Task | None:
        conn = get_connection()
        row = conn.execute(
            """
                SELECT * FROM tasks WHERE id = ?
            """,
            (id,)
        ).fetchone()
        conn.close()
        
        return _row_to_task(row)
    
    def create(self, data: TaskCreate) -> Task:
        conn = get_connection()
        row = conn.execute(
            "INSERT INTO tasks (title) VALUES (?) RETURNING *",
            (data.title,),
        ).fetchone()
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
        conn.execute(
            """
                UPDATE tasks SET title = ?, done = ? 
                WHERE id = ?            
            """, (title,int(done),id,)
        )
        conn.commit()
        conn.close()
        
        return self.findById(id)
    
    def delete(self, id: int) -> bool:
        conn = get_connection()
        cursor = conn.execute("DELETE FROM tasks WHERE id = ?", (id,))
        conn.commit()
        conn.close()
        return cursor.rowcount > 0