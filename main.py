import asyncio
import logging
from bot_cod import bot, dp
from handlers.start import start_router
from handlers.menu import menu_router
from handlers.geolocation import geolocation_router
from handlers.other_messages import other_messages_router


async def main():
    dp.include_router(start_router)
    dp.include_router(menu_router)
    dp.include_router(geolocation_router)
    dp.include_router(other_messages_router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())