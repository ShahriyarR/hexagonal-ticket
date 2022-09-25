from src.domain.model.ticket import Ticket
from src.domain.ports.ticket_repository import TicketRepositoryInterface


class TicketInMemory(TicketRepositoryInterface):
    _tickets: list[Ticket] = []

    def create(self, ticket: Ticket) -> Ticket:
        self._tickets.append(ticket)
        return ticket

    def find_all(self) -> list[Ticket]:
        return self._tickets
