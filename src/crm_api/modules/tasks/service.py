from crm_api.shared.Errors.errors import AppError
from .entities  import TaskRepository
from .schemas   import TaskCreate,TaskUpdate

class TaskService:
    def __init__(self,repository: TaskRepository):
        self.repository = repository
        
    
    def findAll(self):
        return self.repository.findAll()
    
    def findById(self,id:int):
        task = self.repository.findById(id)
        if not task:
            raise AppError("Task not found",404)
        return task
    
    def create(self, data: TaskCreate):
        return self.repository.create(data)
    
    def update(self, data: TaskUpdate, id:int):
        task = self.repository.findById(id)
        if not task:
            raise AppError("Task not found",404)
        
        return self.repository.update(data,id) 
    
    def delete(self, id: int):
        deleted = self.repository.delete(id)
        if not deleted:
            raise AppError("Task não encontrada", 404)