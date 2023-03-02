from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal
from textual.widgets import Footer, Label

from pomotodo.app.widgets.pomodoro_message import PomodoroMessage
from pomotodo.app.widgets.pomodoro_timer import PomodoroTimer
from pomotodo.app.widgets.todo_input import TodoInput
from pomotodo.app.widgets.todo_list import TodoList
from pomotodo.todo_list.unit_of_work import FakeUnitOfWork


class PomotodoApp(App):
    CSS_PATH = "pomotodo.css"
    BINDINGS = [
        ("q", "quit", "Quit"),
    ]

    def compose(self) -> ComposeResult:
        with Container(classes="sidebar"):
            yield TodoInput()
            yield TodoList(uow=FakeUnitOfWork())
        with Horizontal(classes="items-center"):
            yield PomodoroTimer()
        with Horizontal(classes="items-center"):
            yield (PomodoroMessage("Time to focus!", id="message"))
        yield Footer()

    def on_mount(self) -> None:
        self.query_one(PomodoroTimer).focus()

    def on_input_submitted(self, event: TodoInput.Submitted) -> None:
        todo_description: str = event.input.value.strip()
        self.query_one(TodoList).add_todo(description=todo_description)
        self.query_one(TodoInput).value = ""


if __name__ == "__main__":
    app = PomotodoApp()
    app.run()
