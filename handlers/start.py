from aiogram import Router,types,F
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command



start_router = Router()
user_id = set()

@start_router.message(Command("start"))
async def start_handler(message: types.Message):
    nam_id = message.from_user.id
    user_id.add(nam_id)
    count_id = len(user_id)
    name = message.from_user.first_name
    msg = (f"Привет, {name} наш бот обслуживает уже {count_id} пользователя."
           f"Выберите команды /menu, /geolocation /review")

    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text="Оставить отзыв",
                    callback_data="review"
                )
            ]
        ]
    )
    await message.answer(msg, reply_markup=kb)

    kob = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text='/start')
            ]
        ]
    )
    await message.answer('', reply_markup=kob)



@start_router.callback_query(F.data == '/start')
async def start_us(message: types.Message, state: FSMContext):
    kob = types.ReplyKeyboardMarkup()
    await state.update_data(gender=message.text)
    await message.answer("", reply_markup=kob)











