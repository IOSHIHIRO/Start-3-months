from aiogram import Router,types
from aiogram.filters import Command

menu_router=Router()

@menu_router.message(Command('menu'))
async def menu(message: types.Message):
    msg = f'Меню заказа'
    kd = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text='Меню',
                    url='https://glovoapp.com/kg/ru/bishkek/asahi-sushi-bsk/'
                )

            ]

        ]
    )
    await message.answer(msg, reply_markup=kd)