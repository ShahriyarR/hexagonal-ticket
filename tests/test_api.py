import pytest
import json
from flask import url_for

from src.adapters.api import PlacingTicketInputDto
from src.adapters.api.application import create_app


@pytest.fixture
def app():
    app = create_app()
    yield app
    app.container.unwire()


def test_with_no_tickets(client, app):
    response = client.get(url_for("tickets.tickets"))
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data == {'type': 'Success', 'value': '[]'}


def test_create_tickets(client, app):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {"description": "test", "priority": 1}
    response = client.post(url_for("tickets.tickets"), data=json.dumps(data), headers=headers)
    assert "description" in json.loads(response.data)


def test_could_not_create_more_then_three_tickets(client, app):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {"description": "test", "priority": 1}
    client.post(url_for("tickets.tickets"), data=json.dumps(data), headers=headers)
    client.post(url_for("tickets.tickets"), data=json.dumps(data), headers=headers)
    response = client.post(url_for("tickets.tickets"), data=json.dumps(data), headers=headers)
    assert {'message': 'TicketCountException: Ticket count is more than 3',
            'type': 'SystemError'} == json.loads(response.data)


def test_placing_input_dto():
    input_dto = PlacingTicketInputDto(description="test", priority=1)
    assert input_dto.to_dict() == {"description": "test", "priority": 1}
