from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Footer, Input, Label, ListItem

from pomotodo.app.pomodoro_timer import PomodoroTimer
from pomotodo.app.todo_input import TodoInput
from pomotodo.app.todo_list import TodoList


class PomotodoApp(App):
    CSS_PATH = "pomotodo.css"
    BINDINGS = [
        ("q", "quit", "Quit"),
        ("i", "focus_input", "Add Todo"),
        ("t", "focus_todo_list", "Todo List"),
    ]

    def compose(self) -> ComposeResult:
        yield Container(
            TodoInput(),
            TodoList(),
            id="sidebar",
        )
        yield PomodoroTimer()
        yield Footer()

    def on_mount(self) -> None:
        self.query_one(PomodoroTimer).focus()

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
