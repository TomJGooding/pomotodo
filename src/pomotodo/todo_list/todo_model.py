import dataclasses
import uuid


@dataclasses.dataclass
class Todo:
    id: uuid.UUID
    description: str
    complete: bool

    @classmethod
    def from_dict(cls, d: dict):
        return cls(**d)

    def to_dict(self):
        return dataclasses.asdict(self)
