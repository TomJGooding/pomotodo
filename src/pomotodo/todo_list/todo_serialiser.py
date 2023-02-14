import json
from typing import Any


class TodoJsonEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        try:
            to_serialise = {
                "id": str(o.id),
                "description": o.description,
                "complete": o.complete,
            }
            return to_serialise
        except AttributeError:
            return super().default(o)
