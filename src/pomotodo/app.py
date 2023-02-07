from textual.app import App, ComposeResult
from textual.widgets import Footer, Input, Label, ListItem

from pomotodo.countdown_timer import CountdownTimer
from pomotodo.todo_form import TodoForm
from pomotodo.todo_list import TodoList


class PomotodoApp(App):
    BINDINGS = [
        ("q", "quit", "Quit"),
        ("i", "focus_input", "Add Todo"),
        ("t", "focus_todo_list", "Todo List"),
    ]

    def compose(self) -> ComposeResult:
        yield CountdownTimer()
        yield TodoForm()
        yield TodoList()
        yield Footer()

    def on_mount(self) -> None:
        self.query_one(CountdownTimer).focus()

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
