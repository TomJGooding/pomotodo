import json
import uuid

from pomotodo.todo_list.model import Todo
from pomotodo.todo_list.serialiser import TodoJsonEncoder


def test_serialise_todo() -> None:
    id = uuid.uuid4()

    todo = Todo(
        id,
        description="Example todo description",
        complete=False,
    )

    expected_json = f"""
        {{
            "id": "{id}",
            "description": "Example todo description",
            "complete": false
        }}
    """

    json_todo = json.dumps(todo, cls=TodoJsonEncoder)

    assert json.loads(json_todo) == json.loads(expected_json)
