"""employee_handler to verify that the employee does not have another appointment at the same time.

author: Julian David Celis Giraldo <jdcelisg@udistrital.edu.co>

"""

from typing import TYPE_CHECKING
from handlers.handler import Handler  # pylint: disable=import-error
from data_object.cr_res_dto import CreateReservationDTO  # pylint: disable=import-error


if TYPE_CHECKING:
    from services.reservation_service import ReservationService  # Only for type hints


class EmployeeHandler(Handler): # pylint: disable=too-few-public-methods
    """Verifies that the employee does not have another appointment at the same time."""

    def _validate(
        self, reservation: CreateReservationDTO, service: "ReservationService"
    ) -> bool:  # 👈 Quotes in ReservationService
        """Validates that the employee is available at that date and time."""
        existing_reservations = service.get_by_employee(reservation.id_employee)

        for res in existing_reservations:
            if res.reservationDate == reservation.reservationDate:
                raise ValueError(
                    f"The employee {reservation.id_employee} already has an appointment "
                    "at that time."
                )

        return True
