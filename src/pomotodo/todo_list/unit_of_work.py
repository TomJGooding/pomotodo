from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from pomotodo.todo_list.repository import AbstractRepository, MemoryRepository


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


class MemoryUnitOfWork(AbstractUnitOfWork):
    def __init__(self) -> None:
        self.todos = MemoryRepository()
        self.committed = False

    def commit(self) -> None:
        self.committed = True

    def rollback(self) -> None:
        pass
