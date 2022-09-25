from ..model.ticket import Ticket
from .ticket_repository import TicketRepositoryInterface


class TicketCountException(Exception):
    ...


class TicketService:

    def __init__(self, ticket_repo: TicketRepositoryInterface) -> None:
        self.ticket_repo = ticket_repo

    def create(self, description: str, priority: int) -> Ticket:
        ticket = Ticket(description=description, priority=priority)
        if len(self.find_active_tickets()) >= 3:
            raise TicketCountException("Ticket count is more than 3")

        self.ticket_repo.create(ticket)
        return ticket

    def find_all(self) -> list[Ticket]:
        return self.ticket_repo.find_all()

    def find_active_tickets(self) -> list[Ticket]:
        return [ticket for ticket in self.ticket_repo.find_all() if ticket != ticket.is_closed()]
