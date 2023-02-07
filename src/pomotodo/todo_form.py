from textual.app import ComposeResult
from textual.widgets import Input, Static


class TodoForm(Static):
    def compose(self) -> ComposeResult:
        yield Input(placeholder="Add ToDo")
