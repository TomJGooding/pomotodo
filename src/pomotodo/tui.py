from textual.app import App, ComposeResult
from textual.widgets import Footer, Input, Label, ListItem, ListView, Static


class TodoForm(Static):
    def compose(self) -> ComposeResult:
        yield Input(placeholder="Add ToDo")


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


class PomotodoApp(App):
    BINDINGS = [
        ("q", "quit", "Quit"),
        ("i", "focus_input", "Add Todo"),
        ("t", "focus_todo_list", "Todo List"),
    ]

    def compose(self) -> ComposeResult:
        yield TodoForm()
        yield TodoList()
        yield Footer()

    def on_mount(self) -> None:
        self.query_one(Input).focus()

    def action_focus_input(self) -> None:
        self.query_one(Input).focus()

    def action_focus_todo_list(self) -> None:
        self.query_one(TodoList).focus()

    def on_input_submitted(self, event: Input.Submitted) -> None:
        self.query_one(TodoList).append(ListItem(Label(event.value)))
        self.query_one(Input).value = ""


if __name__ == "__main__":
    app = PomotodoApp()
    app.run()
