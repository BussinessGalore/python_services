"""This module contains the CustomerStoreDTO class which is used to define the
data structure related to the customer and the store.

Author: Julian David Celis Giraldo <celisjuliandavid@gmail.com>
"""

from pydantic import BaseModel


class CustomerStoreDTO(BaseModel):
    """This class is used to define the data structure
    related to the customer and the store."""

    id_customer: int
    id_store: int
