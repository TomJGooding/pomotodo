import uuid

from pomotodo.todo_list.model import Todo
from pomotodo.todo_list.unit_of_work import AbstractUnitOfWork


def add_todo(
    id: uuid.UUID,
    description: str,
    complete: bool,
    uow: AbstractUnitOfWork,
) -> None:
    with uow:
        uow.todos.add(Todo(id, description, complete))
        uow.commit()


def get_all_todos(uow: AbstractUnitOfWork) -> list[Todo]:
    with uow:
        todos = uow.todos.list()
    return todos


def change_todo_status(id: uuid.UUID, uow: AbstractUnitOfWork) -> None:
    with uow:
        todo: Todo = uow.todos.get(id)
        todo.complete = not todo.complete
        uow.commit()
