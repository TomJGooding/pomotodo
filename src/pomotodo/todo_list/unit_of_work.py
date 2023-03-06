from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from pomotodo.todo_list.model import Todo
from pomotodo.todo_list.repository import AbstractRepository, FakeRepository


class AbstractUnitOfWork(ABC):
    todos: AbstractRepository

    def __enter__(self) -> AbstractUnitOfWork:
        return self

    def __exit__(self, *args: Any) -> None:
        self.rollback()

    @abstractmethod
    def commit(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def rollback(self) -> None:
        raise NotImplementedError


todo_dicts = [
    {
        "id": "5222f664-71e6-4481-ad38-a7dd37d3636e",
        "description": "Add your todos for today",
        "complete": True,
    },
    {
        "id": "65efd605-5d2b-4888-be71-79c63c275873",
        "description": "Pick a todo and start the timer",
        "complete": False,
    },
    {
        "id": "be9bd462-5978-473b-aeea-443e257060eb",
        "description": "Work on your todo until the time is up",
        "complete": False,
    },
    {
        "id": "ac6a9857-4a82-4590-852f-8c1bd4208570",
        "description": "Take a short break",
        "complete": False,
    },
    {
        "id": "1b57305e-2eb3-431e-81ac-03784b0fdf51",
        "description": "Repeat!",
        "complete": False,
    },
]


class FakeUnitOfWork(AbstractUnitOfWork):
    def __init__(self) -> None:
        self.todos = FakeRepository([Todo.from_dict(todo) for todo in todo_dicts])
        self.committed = False

    def commit(self) -> None:
        self.committed = True

    def rollback(self) -> None:
        pass
