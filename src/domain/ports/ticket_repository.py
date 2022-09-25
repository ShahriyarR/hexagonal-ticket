from abc import ABC, abstractmethod
from ..model.ticket import Ticket


class TicketRepositoryInterface(ABC):

    @abstractmethod
    def create(self, ticket: Ticket) -> Ticket:
        raise NotImplementedError  # pragma: no cover

    @abstractmethod
    def find_all(self) -> list[Ticket]:
        raise NotImplementedError  # pragma: no cover
