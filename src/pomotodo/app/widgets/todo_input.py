from textual.widgets import Input


class TodoInput(Input):
    BINDINGS = [("escape", "cancel", "Cancel")]

    def __init__(self) -> None:
        super().__init__(placeholder="Add Todo")

    def action_cancel(self) -> None:
        self.value = ""
        self.app.query_one("TodoListView").focus()
