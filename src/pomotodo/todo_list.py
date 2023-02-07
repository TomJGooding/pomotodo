from textual.app import ComposeResult
from textual.widgets import Label, ListItem, ListView


class TodoList(ListView):
    BINDINGS = [
        ("k", "cursor_up", "Up"),
        ("j", "cursor_down", "Down"),
    ]

    def __init__(self, todos: list[str] = []) -> None:
        super().__init__()
        self._todos: list[str] = todos

    def compose(self) -> ComposeResult:
        for todo in self._todos:
            yield ListItem(Label(todo))
