import uuid

from pomotodo.todo_list import todo_list_services
from pomotodo.todo_list.todo_list_repository import FakeRepository


class FakeUnitOfWork(todo_list_services.AbstractUnitOfWork):
    def __init__(self):
        self.todos = FakeRepository([])
        self.committed = False

    def commit(self):
        self.committed = True

    def rollback(self):
        pass


def test_add_todo():
    uow = FakeUnitOfWork()
    id = uuid.uuid4()

    todo_list_services.add_todo(
        id=id,
        description="Example todo description",
        complete=False,
        uow=uow,
    )

    assert uow.committed
