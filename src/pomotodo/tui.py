from textual.app import App, ComposeResult
from textual.widgets import Footer, Input, Static


class TodoForm(Static):
    def compose(self) -> ComposeResult:
        yield Input(placeholder="Add ToDo")


class PomotodoApp(App):
    BINDINGS = [("q", "quit", "Quit")]

    def compose(self) -> ComposeResult:
        yield TodoForm()
        yield Footer()

    def on_mount(self) -> None:
        self.query_one(Input).focus()

    def on_input_submitted(self) -> None:
        self.query_one(Input).value = ""


if __name__ == "__main__":
    app = PomotodoApp()
    app.run()
