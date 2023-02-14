from pomotodo.todo_list.todo_model import Todo


class FakeRepository:
    def __init__(self, data) -> None:
        self.data = data

    def list(self):
        return [Todo.from_dict(i) for i in self.data]
