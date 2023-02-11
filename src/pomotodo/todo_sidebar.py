from textual.containers import Container

from pomotodo.todo_input import TodoInput
from pomotodo.todo_list import TodoList


class TodoSidebar(Container):
    def compose(self):
        yield TodoInput()
        yield TodoList()
