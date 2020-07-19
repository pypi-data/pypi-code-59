__version__ = "0.1.0"


"""Imports the Routes and the app and glues them all together"""
from fastapi import APIRouter

from .config import settings
from magicapi.app_factory import create_app, create_handler

app = create_app(config_settings=settings)
handler = create_handler(app)

# this requires a background router
from magicapi.Utils.middleware import CallRoute

router = APIRouter(route_class=CallRoute)


def add_routes(this_app):

    # import all of the routes
    from app import Routes

    this_app.include_router(router)


# add_routes(app)

app.include_router(router)