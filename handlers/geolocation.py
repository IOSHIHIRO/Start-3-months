from aiogram import Router,types
from aiogram.filters import Command

geolocation_router = Router()

@geolocation_router.message(Command('geolocation'))
async def geolocation(message: types.Message):
    msg = f'Контакты и Геолакация'
    kd =types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text='Геолакация',
                    url='https://2gis.kg/bishkek/geo/70030076256308406/74.597262,42.860602'
                ),

                types.InlineKeyboardButton(
                    text='Контактный номер:'
                         '\n +996777777777',
                    callback_data='geolocation'
                )

            ]
        ]
    )
    await message.answer(msg, reply_markup=kd)

