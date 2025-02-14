"""This module is used to define data structure related to reservations.

Author: Julian David Celis Giraldo <celisjuliandavid@gmail.com>
"""

from datetime import datetime
from pydantic import BaseModel

class ReservationDAO(BaseModel):
    """This class is used to define data structure related to reservations."""
    id_reservation: int
    id_employee: int
    id_customer: int
    id_service: int
    id_store: int
    reservationDate: datetime
    status: str
