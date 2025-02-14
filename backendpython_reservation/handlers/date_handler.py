"""
    This module is used for the date handler class to validate the reservation date and time.
    
    Author: Julian David Celis Giraldo <jdcelisg@udistrital.edu.co>

"""

from typing import TYPE_CHECKING
from datetime import datetime, timezone
from handlers.handler import Handler  # pylint: disable=import-error
from data_object.cr_res_dto import CreateReservationDTO  # pylint: disable=import-error

if TYPE_CHECKING:
    from services.reservation_service import (
        ReservationService,
    )  # Evita la importación circular


class DateHandler(Handler): # pylint: disable=too-few-public-methods
    """
    Validates if the date and time have already been registered
    in the same store and that it is not in the past.

    Methods
    -------
    _validate(
        reservation: (
        CreateReservationDTO, service: "ReservationService") -> bool

        Validates that the reservation is in the future and that
        there is no other reservation in the same store at the same time.
    """
    def _validate(
        self, reservation: CreateReservationDTO, service: "ReservationService"
    ) -> bool:
        """
        Validates that the reservation is in the future and that there is no other 
        reservation in the same store at the same time.
        """

        # Convertir a datetime con zona horaria UTC
        if isinstance(reservation.reservationDate, str):
            reservation_datetime = datetime.fromisoformat(
                reservation.reservationDate
            ).replace(tzinfo=timezone.utc)
        else:
            reservation_datetime = reservation.reservationDate.astimezone(timezone.utc)

        # Obtener la hora actual en UTC
        now_utc = datetime.now(timezone.utc)

        # Validar que la reserva esté en el futuro
        if reservation_datetime <= now_utc:
            raise ValueError("No puedes crear una reserva en el pasado.")

        # Validar si ya existe una reserva en la misma tienda a la misma hora
        existing_reservations = service.get_by_store(reservation.id_store)

        for res in existing_reservations:
            # Asegurar que res.reservationDate también tenga zona horaria UTC
            if isinstance(res.reservationDate, str):
                res_datetime = datetime.fromisoformat(res.reservationDate).replace(
                    tzinfo=timezone.utc
                )
            else:
                res_datetime = res.reservationDate.astimezone(timezone.utc)

            # Comparación sin considerar milisegundos
            if res_datetime.replace(microsecond=0) == reservation_datetime.replace(
                microsecond=0
            ):
                raise ValueError(
                    f"Ya existe una reserva en la tienda {reservation.id_store} a esa hora."
                )

        return True
