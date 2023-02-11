from textual.containers import Container

from pomotodo.todo_form import TodoForm
from pomotodo.todo_list import TodoList


class TodoSidebar(Container):
    def compose(self):
        yield TodoForm()
        yield TodoList()
