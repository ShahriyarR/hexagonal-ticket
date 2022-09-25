import json
from dataclasses import dataclass
from typing import Any

from src.domain.model.ticket import TicketJsonEncoder


@dataclass(frozen=True)
class ResponseTypes:
    PARAMETERS_ERROR: str = "ParametersError"
    RESOURCE_ERROR: str = "ResourceError"
    SYSTEM_ERROR: str = "SystemError"
    SUCCESS: str = "Success"


class ResponseFailure:
    def __init__(self, type_, message):
        self.type = type_
        self.message = self._format_message(message)

    def _format_message(self, msg):
        if isinstance(msg, Exception):
            return f"{msg.__class__.__name__}: {msg}"
        return msg

    @property
    def value(self):
        return {"type": self.type, "message": self.message}

    def __bool__(self):
        return False


class ResponseSuccess:
    def __init__(self, value=None):
        self.type = ResponseTypes.SUCCESS
        self.value = value

    def __bool__(self):
        return True


class ResponseFailureJsonEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        try:
            return {"type": o.type, "message": o.message}
        except AttributeError: # pragma: no cover
            return super().default(o)


class ResponseSuccessJsonEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        try:
            return {"type": o.type, "value": json.dumps(o.value, cls=TicketJsonEncoder)}
        except AttributeError: # pragma: no cover
            return super().default(o)
