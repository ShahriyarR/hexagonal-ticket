import json
from dataclasses import dataclass, field, asdict
from uuid import uuid4
from datetime import datetime
from typing import Any


@dataclass(frozen=True)
class TicketStatus:
    OPEN: str = field(default="OPEN")
    IN_PROGRESS: str = field(default="IN_PROGRESS")
    CLOSED: str = field(default="CLOSED")


@dataclass
class Ticket:
    description: str
    priority: int
    id_: str = field(default_factory=uuid4)
    status: TicketStatus = field(default=TicketStatus.OPEN)
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    def is_closed(self) -> bool:
        return self.status == TicketStatus.CLOSED

    def to_dict(self) -> dict[Any]:
        return asdict(self)


class TicketJsonEncoder(json.JSONEncoder):
    def default(self, o):
        try:
            return {
                "description": o.description,
                "priority": o.priority,
                "id": str(o.id_),
                "status": o.status,
                "created_at": str(o.created_at),
                "updated_at": str(o.updated_at),
            }
        except AttributeError:  # pragma: no cover
            return super().default(o)
