"""
This module is used to operate the user reservation service.

Author: Julian David Celis Giraldo <celisjuliandavid@gmail.com>
"""

from datetime import datetime
from typing import List
from handlers.date_handler import DateHandler  # pylint: disable=import-error
from handlers.employee_handler import EmployeeHandler # pylint: disable=import-error
from repositories.reservation_repository import ReservationRepository, ReservationDAO # pylint: disable=import-error
from data_object.customer_store_dto import CustomerStoreDTO # pylint: disable=import-error
from data_object.cr_res_dto import CreateReservationDTO # pylint: disable=import-error

class ReservationService:
    """This class provides services for reservations."""

    def __init__(self):
        self.repository = ReservationRepository()
        self.handler = DateHandler(next_handler=EmployeeHandler()) # Cadena de responsabilidad para validaciones

    def get_all(self) -> List[ReservationDAO]:
        """Returns all reservations."""
        return self.repository.get_all_reservations()

    def get_by_reservation(self, id_reservation: int) -> List[ReservationDAO]:
        """
        Returns a reservation by its id.

        Args:
            id_reservation (int): The ID of the reservation.

        Returns:
            List[ReservationDAO]: A list of reservations matching the ID.
        """
        response = []
        for reservation in self.repository.get_all_reservations():
            if id_reservation == reservation.id_reservation:
                response.append(reservation)
        return response

    def get_by_employee(self, id_employee: int) -> List[ReservationDAO]:
        """
        Returns reservations of an employee.

        Args:
            id_employee (int): The ID of the employee.

        Returns:
            List[ReservationDAO]: A list of reservations for the employee.
        """
        response = []
        for reservation in self.repository.get_all_reservations():
            if id_employee == reservation.id_employee:
                response.append(reservation)
        return response

    def get_by_customer(self, id_customer: int) -> List[ReservationDAO]:
        """
        Returns reservations of a customer.

        Args:
            id_customer (int): The ID of the customer.

        Returns:
            List[ReservationDAO]: A list of reservations for the customer.
        """
        response = []
        for reservation in self.repository.get_all_reservations():
            if id_customer == reservation.id_customer:
                response.append(reservation)
        return response

    def get_by_service(self, id_service: int) -> List[ReservationDAO]:
        """
        Returns reservations of a service.

        Args:
            id_service (int): The ID of the service.

        Returns:
            List[ReservationDAO]: A list of reservations for the service.
        """
        response = []
        for reservation in self.repository.get_all_reservations():
            if id_service == reservation.id_service:
                response.append(reservation)
        return response

    def get_by_store(self, id_store: int) -> List[ReservationDAO]:
        """
        Returns reservations of a store.

        Args:
            id_store (int): The ID of the store.

        Returns:
            List[ReservationDAO]: A list of reservations for the store.
        """
        response = []
        for reservation in self.repository.get_all_reservations():
            if id_store == reservation.id_store:
                response.append(reservation)
        return response

    def get_by_date(self, reservation_date: datetime) -> List[ReservationDAO]:
        """
        Returns reservations of a specific date.

        Args:
            reservation_date (datetime): The date of the reservation.

        Returns:
            List[ReservationDAO]: A list of reservations for the date.
        """
        response = []
        for reservation in self.repository.get_all_reservations():
            if reservation_date == reservation.reservationDate:
                response.append(reservation)
        return response

    def get_by_status(self, status: str) -> List[ReservationDAO]:
        """
        Returns reservations matching the provided status.

        Args:
            status (str): The status of the reservation.

        Returns:
            List[ReservationDAO]: A list of reservations with the status.
        """
        return [
            res
            for res in self.repository.get_all_reservations()
            if res.status == status
        ]

    def get_by_customer_store(self, data: CustomerStoreDTO) -> List[ReservationDAO]:
        """
        Returns reservations of a customer in a store.

        Args:
            data (CustomerStoreDTO): The customer and store data.

        Returns:
            List[ReservationDAO]: A list of reservations for the customer in the store.
        """
        all_reservations = self.repository.get_all_reservations()

        customer_reservations = [
            reservation for reservation in all_reservations
            if reservation.customer_id == data.customer_id and reservation.store_id == data.store_id
        ]

        return customer_reservations
    def create_reservation(self, reservation_dto: CreateReservationDTO) -> ReservationDAO:
        """Crea una reserva después de validaciones en cadena."""

        date_handler = DateHandler(next_handler=EmployeeHandler())
        
        date_handler.validate(reservation_dto, self)

        existing_reservations = self.repository.get_all_reservations()
        new_id = max([res.id_reservation for res in existing_reservations], default=0) + 1

        new_reservation = ReservationDAO(
            id_reservation=new_id,
            id_employee=reservation_dto.id_employee,
            id_customer=reservation_dto.id_customer,
            id_service=reservation_dto.id_service,
            id_store=reservation_dto.id_store,
            reservationDate=reservation_dto.reservationDate,
            status="scheduled"
        )

        # Guardar reserva
        self.repository.add_reservation(new_reservation)

        return new_reservation
