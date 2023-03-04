import uuid

from pomotodo.todo_list.model import Todo
from pomotodo.todo_list.repository import FakeRepository
from pomotodo.todo_list.services import add_todo, change_todo_status, get_all_todos
from pomotodo.todo_list.unit_of_work import AbstractUnitOfWork

todo_dicts = [
    {
        "id": "5222f664-71e6-4481-ad38-a7dd37d3636e",
        "description": "Todo 1 description",
        "complete": False,
    },
    {
        "id": "65efd605-5d2b-4888-be71-79c63c275873",
        "description": "Todo 2 description",
        "complete": False,
    },
    {
        "id": "be9bd462-5978-473b-aeea-443e257060eb",
        "description": "Todo 3 description",
        "complete": False,
    },
]


class FakeUnitOfWork(AbstractUnitOfWork):
    def __init__(self):
        self.todos = FakeRepository([Todo.from_dict(todo) for todo in todo_dicts])
        self.committed = False

    def commit(self):
        self.committed = True

    def rollback(self):
        pass


def test_add_todo():
    uow = FakeUnitOfWork()
    id = uuid.uuid4()

    add_todo(
        id=id,
        description="Example todo description",
        complete=False,
        uow=uow,
    )

    assert uow.todos.get(id) is not None
    assert uow.committed


def test_get_all_todos():
    uow = FakeUnitOfWork()

    todos = [Todo.from_dict(i) for i in todo_dicts]

    assert get_all_todos(uow) == todos


def test_change_todo_status():
    uow = FakeUnitOfWork()
    id = uuid.uuid4()

    add_todo(
        id=id,
        description="Todo to complete",
        complete=False,
        uow=uow,
    )

    change_todo_status(id=id, uow=uow)
    assert uow.todos.get(id).complete is True
