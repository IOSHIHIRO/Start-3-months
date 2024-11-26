import asyncio
import logging

from bot_cod import bot, dp, database
from handlers import private_router
from handlers.group_check import grou_check_router


async def on_startup(bot):
    database.create_tables()


async def main():
    dp.include_router(private_router)
    dp.include_router(grou_check_router)

    dp.startup.register(on_startup)

    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())