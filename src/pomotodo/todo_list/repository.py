import uuid
from abc import ABC, abstractmethod

from pomotodo.todo_list.model import Todo


class AbstractRepository(ABC):
    @abstractmethod
    def add(self, todo: Todo) -> None:
        raise NotImplementedError

    @abstractmethod
    def get(self, id: uuid.UUID) -> Todo:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> list[Todo]:
        raise NotImplementedError


class MemoryRepository(AbstractRepository):
    def __init__(self, todos: list[Todo] = []) -> None:
        self._todos = todos

    def add(self, todo: Todo) -> None:
        self._todos.append(todo)

    def get(self, id: uuid.UUID) -> Todo:
        return next(todo for todo in self._todos if todo.id == id)

    def list(self) -> list[Todo]:
        return self._todos
