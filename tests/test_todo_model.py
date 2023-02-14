import uuid

from pomotodo.todo_model import Todo


def test_todo_model_init():
    id = uuid.uuid4()

    todo = Todo(
        id,
        description="Example todo description",
        complete=False,
    )

    assert todo.id == id
    assert todo.description == "Example todo description"
    assert todo.complete is False


def test_todo_model_from_dict():
    id = uuid.uuid4()
    init_dict = {
        "id": id,
        "description": "Example todo description",
        "complete": False,
    }

    todo = Todo.from_dict(init_dict)

    assert todo.id == id
    assert todo.description == "Example todo description"
    assert todo.complete is False


def test_todo_model_to_dict():
    id = uuid.uuid4()
    init_dict = {
        "id": id,
        "description": "Example todo description",
        "complete": False,
    }

    todo = Todo.from_dict(init_dict)

    assert todo.to_dict() == init_dict


def test_todo_model_comparison():
    id = uuid.uuid4()
    init_dict = {
        "id": id,
        "description": "Example todo description",
        "complete": False,
    }

    todo_1 = Todo.from_dict(init_dict)
    todo_2 = Todo.from_dict(init_dict)

    assert todo_1 == todo_2
