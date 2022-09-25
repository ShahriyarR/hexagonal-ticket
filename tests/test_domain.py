import pytest
import json
from src.domain.model.ticket import Ticket, TicketJsonEncoder


def test_if_default_ticket_status_is_open():
    ticket = Ticket(description="test", priority=1)
    assert not ticket.is_closed()


def test_domain_json_encoder():
    ticket = Ticket(description="test", priority=1)
    assert json.dumps(ticket, cls=TicketJsonEncoder)
