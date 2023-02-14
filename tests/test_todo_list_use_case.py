import uuid
from unittest import mock

import pytest

from pomotodo.todo_list_use_case import todo_list_use_case
from pomotodo.todo_model import Todo


@pytest.fixture
def domain_todos():
    todo_1 = Todo(
        id=uuid.uuid4(),
        description="Todo 1 description",
        complete=False,
    )
    todo_2 = Todo(
        id=uuid.uuid4(),
        description="Todo 2 description",
        complete=False,
    )
    todo_3 = Todo(
        id=uuid.uuid4(),
        description="Todo 3 description",
        complete=False,
    )

    return [todo_1, todo_2, todo_3]


def test_todo_list_without_parameters(domain_todos):
    repo = mock.Mock()
    repo.list.return_value = domain_todos

    result = todo_list_use_case(repo)

    repo.list.assert_called_with()
    assert result == domain_todos
