from aiogram import Router,types
from aiogram.filters import Command

start_router = Router()
user_id = set()
names = ['Люси', 'Майн', 'Хюрезен']



@start_router.message(Command("start"))
async def start_handler(message: types.Message):
    nam_id = message.from_user.id
    user_id.add(nam_id)
    count_id = len(user_id)
    name = message.from_user.first_name
    msg = f"Привет, {name} наш бот обслуживает уже {count_id} пользователя"
    await message.answer(msg)