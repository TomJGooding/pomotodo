from textual.app import ComposeResult
from textual.widgets import Label, ListItem

from pomotodo.todo_list.model import Todo


class TodoItem(ListItem):
    def __init__(self, todo: Todo, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.todo: Todo = todo

    def compose(self) -> ComposeResult:
        if self.todo.complete:
            todo_label = f"\[x] [strike]{self.todo.description}[/strike]"
        else:
            todo_label = f"\[ ] {self.todo.description}"

        yield (Label(todo_label))
