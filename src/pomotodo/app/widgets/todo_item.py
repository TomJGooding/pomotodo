import uuid

from textual.widgets import ListItem


class TodoItem(ListItem):
    def __init__(self, uuid_id: uuid.UUID, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.uuid: uuid.UUID = uuid_id
