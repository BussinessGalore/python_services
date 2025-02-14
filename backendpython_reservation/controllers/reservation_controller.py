"""This module is used to manage the endpoints of the reservation entity."""

from typing import List
from fastapi import APIRouter, HTTPException, Query  # pylint: disable=import-error
from repositories.reservation_repository import ReservationDAO # pylint: disable=import-error
from services.reservation_service import ReservationService # pylint: disable=import-error
from data_object.cr_res_dto import CreateReservationDTO # pylint: disable=import-error
from data_object.customer_store_dto import CustomerStoreDTO # pylint: disable=import-error
router = APIRouter()

services = ReservationService()

@router.get("/")
async def root():
    """This method is used for verify the API is working."""
    return {"message": "API funcionando"}

@router.get("/reservations/all")
def get_all() -> List[ReservationDAO]:
    """This method is used to get all reservations.
    """
    return services.get_all()

@router.get("reservation/by_id_customer")
def get_by_customer(id_customer: int = Query(..., title="ID del Cliente")) -> List[ReservationDAO]:
    """Obtiene las reservas de un cliente por su ID usando query params."""

    if id_customer is None:
        raise HTTPException(status_code=400, detail="El ID del cliente no puede estar vacío.")

    return services.get_by_customer(id_customer)

@router.get("/reservations/actives")
def get_status() -> List[ReservationDAO]:
    """Obtiene las reservas activas (agendadas)."""
    return services.get_by_status("scheduled")

@router.get("/reservations/actives/{id_customer}/{id_store}")
def get_active_by_store_customer(id_customer: int, id_store: int) -> List[ReservationDAO]:
    """Obtiene las reservas activas (agendadas) de un cliente en una tienda."""
    data = CustomerStoreDTO(id_customer=id_customer, id_store=id_store)
    return services.get_by_customer_store_active(data)

@router.post("/reservations/")
def create_reservation(reservation: CreateReservationDTO) -> ReservationDAO:
    """Crea una nueva reserva después de validaciones."""
    try:
        return services.create_reservation(reservation)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e
