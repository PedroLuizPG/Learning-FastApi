from fastapi import APIRouter
from .schemas import TaskOut,TaskCreate,TaskUpdate
from .service import TaskService
from .sqlite_repository import SqliteRepository

router = APIRouter(prefix="/tasks", tags=["tasks"])

# composition root: único lugar de todo o módulo que conhece a
# implementação CONCRETA (SqliteTaskRepository). É aqui, e só aqui,
# que o contrato TaskRepository é "preenchido" por uma escolha real.

service = TaskService(SqliteRepository())

@router.get("/", response_model=list[TaskOut])
def listTasks():
    return service.findAll()

@router.get("/{id}", response_model=TaskOut)
def findOneTask(id:int):
    print(id)
    return service.findById(id)

@router.post("/", response_model=TaskOut, status_code=201)
def createTask(data:TaskCreate):
    return service.create(data)

@router.put("/{id}", response_model=TaskOut)
def updateTask(data:TaskUpdate,id:int):
    return service.update(data,id)

@router.delete("/{id}", status_code=204)
def deleteTask(id: int):
    service.delete(id)