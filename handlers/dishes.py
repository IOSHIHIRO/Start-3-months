from aiogram import F,Router,types
from aiogram.filters import Command

from bot_cod import database
from pprint import pprint

dishes_router=Router()

@dishes_router.message(Command("dishes"))
async def show_all_dishes(message: types.Message):
    all_categories = database.fetch("SELECT * FROM dish_categories")
    if not all_categories:
        await message.answer("Нет ни одного категории")
        return
    kd = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text=category_id["name"]) for category_id in all_categories]
        ]
    )
    await message.answer("Выберите категории", reply_markup=kd)

def dishes_filter(message: types.Message):
    print("inside genre filter")
    all_categories = database.fetch(
        "SELECT name FROM dish_categories WHERE name = ?",
            params=(message.text,))
    if all_categories:
        return True

    return False


@dishes_router.message(dishes_filter)
async def dishes(message: types.Message):
    dishes_all = database.fetch (
        query="SELECT * FROM dishes JOIN dish_categories ON dishes.category_id = dish_categories.id WHERE dish_categories.name = ?",
        params=(message.text,)
    )

    pprint(dishes_all)
    await message.answer("Блюдо из католога: ")
    for dish in dishes_all:
        await message.answer(f'Название: {dish["name"]} \n Цена: {dish["price"]} '
                             f'\n категория: {dish["category_id"]}')