"""Main module of the project.

Author: Carlos Andres Sierra <cavirguezs@udistrital.edu.co>
"""

from fastapi import FastAPI

from controllers import reservation_router #pylint: disable=import-error

app = FastAPI(
    title="Machines and Videogames",
    description="This project is used to manage machines and videogames.",
    version="0.0.1",
)

app.include_router(reservation_router)
