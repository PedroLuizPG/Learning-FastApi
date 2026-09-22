from dataclasses import dataclass
from datetime import datetime
from typing import Protocol


@dataclass
class Task:
    id: int
    tittle: str
    done: bool
    created_at: datetime
    
class TaskRepository(Protocol):
    """
    Contrato que o Service confia. Qualquer classe que tenha estes
    métodos, com esta assinatura, pode ser plugada aqui embaixo —
    SQLite, Postgres, um mock em memória para testes, o que for.
    O Service nunca importa uma implementação concreta, só este Protocol.
    """
    
    def find_all(self) -> list[Task]: ...
    def findById(self,id: int) -> Task | None: ...
    def create(self, data: TaskCreate) -> Task: ...
    def update(self, id:int, data: TaskUpdate) -> Task | None: ...
    def delete(self, id:int) -> bool: ...