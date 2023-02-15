import uuid

from pomotodo.todo_list.todo_list_repository import FakeRepository
from pomotodo.todo_list.todo_list_services import add_todo
from pomotodo.todo_list.unit_of_work import AbstractUnitOfWork


class FakeUnitOfWork(AbstractUnitOfWork):
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

    add_todo(
        id=id,
        description="Example todo description",
        complete=False,
        uow=uow,
    )

    assert uow.committed
