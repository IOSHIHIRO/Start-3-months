from aiogram import F,Router,types
from aiogram.filters import Command

from bot_cod import database
from pprint import pprint

dishes_router=Router()

@dishes_router.message(Command("dishes"))
async def dishes(message: types.Message):
    dishes_all = database.fetch (
        query="SELECT * FROM dishes"
    )
    pprint(dishes_all)
    await message.answer("Блюдо из католога: ")
    for dish in dishes_all:
        await message.answer(f'Название: {dish["name"]} \n Цена: {dish["price"]} '
                             f'\n категория: {dish["category"]}')