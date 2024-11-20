from aiogram import F,Router,types
from aiogram.fsm.state import State, StatesGroup,default_state
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command

from bot_cod import database

bot_administrator_router = Router()
bot_administrator_router.message.filter(
    F.from_user.id == 1627653043
)

class Admin(StatesGroup):
    name = State()
    price = State()
    recipe = State()

@bot_administrator_router.message(Command("dish"), default_state)
async def create_dish(message: types.Message, state: FSMContext):
    print(message.from_user.id)
    await  state.set_state(Admin.name)
    await  message.answer('Задайте название блюдо: ')

@bot_administrator_router.message(Admin.name)
async def create_dish(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Admin.price)
    await message.answer('Задайте цену: ')

@bot_administrator_router.message(Admin.price)
async def create_dish(message: types.Message, state: FSMContext):
    await state.update_data(price=message.text)
    await state.set_state(Admin.recipe)
    await message.answer('Задайте рецепт: ')

@bot_administrator_router.message(Admin.recipe)
async def create_dish(message: types.Message, state: FSMContext):
    await state.update_data(recipe=message.text)

    data = await state.get_data()
    database.execute(
        query="""
        INSERT INTO dishes(name, price, recipe) VALUES (?,?,?)
        """,
        params=(data['name'], data['price'], data['recipe']),
    )
    await state.clear()
    await message.answer('Блюдо добавлено')

