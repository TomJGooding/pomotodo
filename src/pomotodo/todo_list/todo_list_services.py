from __future__ import annotations

import uuid
from abc import ABC, abstractmethod

from pomotodo.todo_list import todo_list_repository, todo_model


class AbstractUnitOfWork(ABC):
    todos: todo_list_repository.AbstractRepository

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


def add_todo(
    id: uuid.UUID,
    description: str,
    complete: bool,
    uow: AbstractUnitOfWork,
):
    with uow:
        uow.todos.add(todo_model.Todo(id, description, complete))
        uow.commit()
