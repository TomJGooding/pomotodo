from pomotodo.todo_model import Todo


class TodoListMemRepo:
    def __init__(self, data) -> None:
        self.data = data

    def list(self):
        return [Todo.from_dict(i) for i in self.data]
