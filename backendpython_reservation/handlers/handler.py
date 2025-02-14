"""Module that contains the base class for validation handlers."""

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
from data_object.cr_res_dto import CreateReservationDTO  # pylint: disable=import-error

if TYPE_CHECKING:
    from services.reservation_service import ReservationService  # Only for type hints


class Handler(ABC): # pylint: disable=too-few-public-methods
    """Base class for validation handlers."""

    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def validate(
        self, reservation: CreateReservationDTO, service: "ReservationService"
    ):
        """Executes the current validation and passes to the next handler if it exists."""
        if not self._validate(reservation, service):
            raise ValueError(f"Validation failed in {self.__class__.__name__}")

        if self.next_handler:
            self.next_handler.validate(reservation, service)

    @abstractmethod
    def _validate(
        self, reservation: CreateReservationDTO, service: "ReservationService"
    ) -> bool:
        """Abstract method that each handler must implement."""
