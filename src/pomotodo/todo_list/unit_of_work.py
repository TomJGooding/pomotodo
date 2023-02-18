from __future__ import annotations

from abc import ABC, abstractmethod

from pomotodo.todo_list.repository import AbstractRepository


class AbstractUnitOfWork(ABC):
    todos: AbstractRepository

    def __enter__(self) -> AbstractUnitOfWork:
        return self

    def __exit__(self, *args):
        self.rollback()

    @abstractmethod
    def commit(self):
        raise NotImplementedError

    @abstractmethod
    def rollback(self):
        raise NotImplementedError
