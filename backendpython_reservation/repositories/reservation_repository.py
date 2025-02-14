"""
This module defines the ReservationRepository class, 
which is responsible for managing reservation data.

Author: Julian David Celis Giraldo <celisjuliandavid@gmail.com>
"""

import json
from typing import List
from environment_variables import EnvironmentVariables  # pylint: disable=import-error
from data_object.reservation_dao import ReservationDAO  # pylint: disable=import-error


class ReservationRepository:
    """This class is used to manage reservation data."""

    def __init__(self):
        """This method is used to initialize the class."""
        path_file = EnvironmentVariables().path_reservation_data
        self.path_file = path_file
        self._load_data(path_file)

    def _load_data(self, path_file: str):
        try:
            with open(path_file, "r", encoding="utf-8") as f:
                self.data = json.load(f)
        except FileNotFoundError:
            print("File not found")
            self.data = []

    def _save_data(self):
        """Guarda las reservas en el archivo JSON."""
        with open(self.path_file, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=4, default=str)

    def add_reservation(self, reservation: ReservationDAO):
        """Guarda la reserva en el archivo JSON."""
        self.data.append(
            reservation.model_dump()
        )
        self._save_data()

    def get_all_reservations(self) -> List[ReservationDAO]:
        """This method is used to get all reservations."""
        reservations = []
        for reservation in self.data:
            reservation_temp = ReservationDAO(
                id_reservation=reservation["id_reservation"],
                id_employee=reservation["id_employee"],
                id_customer=reservation["id_customer"],
                id_service=reservation["id_service"],
                id_store=reservation["id_store"],
                reservationDate=reservation["reservationDate"],
                status= "sheduled"
            )
            reservations.append(reservation_temp)
        return reservations
