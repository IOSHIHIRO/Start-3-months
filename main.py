import asyncio
import logging

from bot_cod import bot, dp, database
from handlers.start import start_router
from handlers.menu import menu_router
from handlers.geolocation import geolocation_router
from handlers.review_dialog import review_router
from handlers.other_messages import other_messages_router
from handlers.bot_administrator import bot_administrator_router
from handlers.dishes import dishes_router


async def on_startup(bot):
    database.create_tables()



async def main():
    dp.include_router(start_router)
    dp.include_router(menu_router)
    dp.include_router(geolocation_router)
    dp.include_router(review_router)
    dp.include_router(bot_administrator_router)
    dp.include_router(dishes_router)

    dp.include_router(other_messages_router)

    dp.startup.register(on_startup)

    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())