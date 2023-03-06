from __future__ import annotations

import dataclasses
import uuid


@dataclasses.dataclass
class Todo:
    id: uuid.UUID
    description: str
    complete: bool

    @classmethod
    def from_dict(cls, d: dict) -> Todo:
        return cls(**d)

    def to_dict(self) -> dict:
        return dataclasses.asdict(self)
