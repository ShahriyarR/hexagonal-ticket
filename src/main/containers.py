from dependency_injector import containers, providers
from src.domain.ports.ticket_service import TicketService
from src.adapters.db.in_memory_repository import TicketInMemory


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(packages=["src.adapters.api.blueprints"])

    in_memory_repo = TicketInMemory()

    ticket_service = providers.Factory(
        TicketService,
        ticket_repo=in_memory_repo
    )
