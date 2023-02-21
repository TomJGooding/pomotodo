import uuid

from textual.reactive import reactive
from textual.widgets import ListView

from pomotodo.app.widgets.todo_item import TodoItem
from pomotodo.todo_list import services
from pomotodo.todo_list.model import Todo
from pomotodo.todo_list.unit_of_work import AbstractUnitOfWork


class TodoList(ListView):
    BINDINGS = [
        ("k", "cursor_up", "Up"),
        ("j", "cursor_down", "Down"),
    ]

    todos: reactive[list[Todo]] = reactive([])

    def __init__(self, uow: AbstractUnitOfWork) -> None:
        super().__init__()
        self.uow: AbstractUnitOfWork = uow
        self.load_todos()

    def load_todos(self) -> None:
        todos = services.get_all_todos(uow=self.uow)
        for todo in todos:
            self.append(TodoItem(todo))

    def add_todo(self, description: str) -> None:
        services.add_todo(
            id=uuid.uuid4(),
            description=description,
            complete=False,
            uow=self.uow,
        )
        self.clear()
        self.load_todos()
