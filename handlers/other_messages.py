from aiogram import Router,types

other_messages_router = Router()



@other_messages_router.message()
async def echo_handler(message: types.Message):
    name = message.from_user.first_name
    await message.answer(f'Нет такой команды! Пользователь {name} '
                         f' Выберите команду /start, /menu, /geolocation')
