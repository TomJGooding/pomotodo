from abc import ABC, abstractmethod

from pomotodo.todo_list import todo_model
from pomotodo.todo_list.todo_model import Todo


class AbstractRepository(ABC):
    @abstractmethod
    def add(self, todo: todo_model.Todo):
        raise NotImplementedError


class FakeRepository(AbstractRepository):
    def __init__(self, data: list[dict]) -> None:
        self.data: list[dict] = data

    def add(self, todo) -> None:
        self.data.append(todo.to_dict())

    def list(self) -> list[Todo]:
        return [Todo.from_dict(i) for i in self.data]
