""" this module is used to create a data transfer object (DTO) 
to receive data when creating a reservation. 

Author: Julian David Celis Giraldo <jdcelisg@udistrital.edu.co
"""

from datetime import datetime
from pydantic import BaseModel, Field


class CreateReservationDTO(BaseModel):
    """
    CreateReservationDTO is a Data Transfer Object (DTO)
    used to receive data when creating a reservation.
    """
    id_employee: int = Field(..., gt=0, description="ID del empleado")
    id_customer: int = Field(..., gt=0, description="ID del cliente")
    id_service: int = Field(..., gt=0, description="ID del servicio")
    id_store: int = Field(..., gt=0, description="ID de la tienda")
    reservationDate: datetime = Field(..., description="Fecha y hora de la reserva")
