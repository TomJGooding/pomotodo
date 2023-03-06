import uuid

from textual.widgets import ListView

from pomotodo.app.widgets.todo_item import TodoItem
from pomotodo.todo_list import services
from pomotodo.todo_list.unit_of_work import AbstractUnitOfWork


class TodoListView(ListView):
    BINDINGS = [
        ("i", "focus_todo_input", "Add Todo"),
        ("k", "cursor_up", "Up"),
        ("j", "cursor_down", "Down"),
        ("x", "mark_complete", "Mark complete"),
        ("t", "focus_pomodoro_timer", "Timer"),
    ]

    def __init__(self, uow: AbstractUnitOfWork) -> None:
        super().__init__()
        self.uow: AbstractUnitOfWork = uow
        self.load_todos()

    def load_todos(self) -> None:
        highlighted_index = self.index
        self.clear()
        todos = services.get_all_todos(uow=self.uow)
        for todo in todos:
            self.append(TodoItem(todo))
        self.index = highlighted_index

    def add_todo(self, description: str) -> None:
        services.add_todo(
            id=uuid.uuid4(),
            description=description,
            complete=False,
            uow=self.uow,
        )
        self.load_todos()

    def action_mark_complete(self) -> None:
        highlighted_todo: TodoItem | None = (
            self.highlighted_child  # type: ignore[assignment]
        )
        if not highlighted_todo:
            return

        todo_id: uuid.UUID = highlighted_todo.todo.id
        services.change_todo_status(todo_id, self.uow)
        self.load_todos()

    def action_focus_pomodoro_timer(self) -> None:
        self.app.query_one("PomodoroTimer").focus()

    def action_focus_todo_input(self) -> None:
        self.app.query_one("TodoInput").focus()
