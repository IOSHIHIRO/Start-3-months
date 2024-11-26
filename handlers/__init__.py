from aiogram import Router, F

from .start import start_router
from .menu import menu_router
from .bot_administrator import bot_administrator_router
from .geolocation import geolocation_router
from .dishes import dishes_router
from .review_dialog import review_router
from .other_messages import other_messages_router

private_router = Router()
private_router.include_router(start_router)
private_router.include_router(menu_router)
private_router.include_router(dishes_router)
private_router.include_router(review_router)
private_router.include_router(geolocation_router)
private_router.include_router(other_messages_router)

private_router.message.filter(F.chat.type == 'private')
private_router.callback_query.filter(F.chat.type == 'private')
