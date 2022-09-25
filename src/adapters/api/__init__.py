from dataclasses import dataclass, asdict


@dataclass
class PlacingTicketInputDto:
    description: str
    priority: int

    def to_dict(self):
        return asdict(self)
