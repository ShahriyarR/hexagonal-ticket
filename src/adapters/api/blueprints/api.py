import json

from flask import Blueprint, request, Response
from dependency_injector.wiring import inject, Provide

from src.adapters.api import PlacingTicketInputDto
from src.domain.ports.ticket_service import TicketService
from src.main.containers import Container
from .responses import ResponseFailure, ResponseSuccess, ResponseSuccessJsonEncoder, ResponseTypes, \
    ResponseFailureJsonEncoder

blueprint = Blueprint("tickets", __name__)


@blueprint.route("/tickets", methods=["GET", "POST"])
@inject
def tickets(ticket_service: TicketService = Provide[Container.ticket_service]):
    if request.method == "POST":
        content = request.json
        input_dto = PlacingTicketInputDto(description=content["description"], priority=content["priority"])

        try:
            ticket = ticket_service.create(input_dto.description, input_dto.priority)
        except Exception as exc:
            result = ResponseFailure(ResponseTypes.SYSTEM_ERROR, exc)
            return Response(
                json.dumps(result, cls=ResponseFailureJsonEncoder),
                mimetype="application/json",
                status=500
            )
        return ticket.to_dict()

    if request.method == "GET":
        result = ResponseSuccess(ticket_service.find_all())
        return Response(
            json.dumps(result, cls=ResponseSuccessJsonEncoder),
            mimetype="application/json",
            status=200
        )
