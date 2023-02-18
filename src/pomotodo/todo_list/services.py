import uuid

from pomotodo.todo_list.model import Todo
from pomotodo.todo_list.unit_of_work import AbstractUnitOfWork


def add_todo(
    id: uuid.UUID,
    description: str,
    complete: bool,
    uow: AbstractUnitOfWork,
):
    with uow:
        uow.todos.add(Todo(id, description, complete))
        uow.commit()
