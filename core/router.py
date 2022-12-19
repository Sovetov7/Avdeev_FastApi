from fastapi import FastAPI
from App.routers import student
from App.routers import group


def set_routers(app: FastAPI):
    app.include_router(student.router, prefix="", tags=[])
    app.include_router(group.router, prefix="", tags=[])
