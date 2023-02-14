import pytest

from pomotodo.todo_list.todo_list_repository import TodoListMemRepo
from pomotodo.todo_list.todo_model import Todo


@pytest.fixture
def todo_dicts():
    return [
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


def test_repository_list_without_parameters(todo_dicts):
    repo = TodoListMemRepo(todo_dicts)

    todos = [Todo.from_dict(i) for i in todo_dicts]

    assert repo.list() == todos
