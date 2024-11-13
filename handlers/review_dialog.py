from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

review_router = Router()

class RestourantReview(StatesGroup):
    name = State()
    phone_number = State()
    visit_date = State()
    food_rating = State()
    cleanliness_rating = State()
    extra_comments = State()


def cleanliness_keyboard():
    return types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text="5",
                    callback_data="5"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text="4",
                    callback_data="4"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text="3",
                    callback_data="3"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text="2",
                    callback_data="2"
                )
            ]
        ]
    )


@review_router.message(Command('review'))
async def start_opros(message: types.Message, state: FSMContext):
    await state.set_state(RestourantReview.name)
    await message.answer('Как вас зовут? ')


@review_router.message(RestourantReview.name)
async def process_opros(message: types.Message, state: FSMContext):
    name = message.text
    if not name.istitle():
        await message.answer('Имя должно начинаться с заглавной буквы.')
        return

    await state.update_data(name=message.text)
    await state.set_state(RestourantReview.phone_number)
    await message.answer('Укажите ваш номер: ')


@review_router.message(RestourantReview.phone_number)
async def process_opros(message: types.Message, state: FSMContext):
    number = message.text
    if not number.isdigit():
        await message.answer("Вводите только цифры")
        return

    await state.update_data(phone_number=message.text)
    await state.set_state(RestourantReview.visit_date)
    await message.answer('Дата вашего посещения нашего заведения: ')


@review_router.message(RestourantReview.visit_date)
async def process_opros(message: types.Message, state: FSMContext):
    await state.update_data(visit_date=message.text)
    await state.set_state(RestourantReview.food_rating)
    msg = "Как оцениваете качество еды: "
    kd = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text='плохо',
                    callback_data='badly'
                ),
                types.InlineKeyboardButton(
                    text='удовлетворительно',
                    callback_data='satisfactorily'
                ),
                types.InlineKeyboardButton(
                    text='хорошо',
                    callback_data='fine'
                ),
                types.InlineKeyboardButton(
                    text='отлично',
                    callback_data='Great'
                )
            ]
        ]
    )
    await message.answer(msg, reply_markup=kd)


@review_router.callback_query(F.data == 'badly')
async def badly_us(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(food_rating="badly")
    await callback.message.answer('Спасибо за отзыв')
    await state.set_state(RestourantReview.cleanliness_rating)
    await callback.message.answer("Оцените чистоту нашего заведения", reply_markup=cleanliness_keyboard())


@review_router.callback_query(F.data == 'satisfactorily')
async def badly_us(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(food_rating="satisfactorily")
    await callback.message.answer('Спасибо за отзыв')
    await state.set_state(RestourantReview.cleanliness_rating)
    await callback.message.answer("Оцените чистоту нашего заведения", reply_markup=cleanliness_keyboard())


@review_router.callback_query(F.data == 'fine')
async def badly_us(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(food_rating="fine")
    await callback.message.answer('Спасибо за отзыв')
    await state.set_state(RestourantReview.cleanliness_rating)
    await callback.message.answer("Оцените чистоту нашего заведения", reply_markup=cleanliness_keyboard())


@review_router.callback_query(F.data == 'Great')
async def badly_us(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(food_rating="Great")
    await callback.message.answer('Спасибо за отзыв')
    await state.set_state(RestourantReview.cleanliness_rating)
    await callback.message.answer("Оцените чистоту нашего заведения", reply_markup=cleanliness_keyboard())


@review_router.message(RestourantReview.cleanliness_rating)
async def cleanliness_us(message: types.Message, state: FSMContext):
    await state.update_data(cleanliness_rating=message.text)
    await state.set_state(RestourantReview.extra_comments)
    await message.answer('Как оцениваете чистоту заведения ')


@review_router.callback_query(F.data == '5')
async def badly_us(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(cleanliness_rating='5')
    await state.set_state(RestourantReview.extra_comments)
    await callback.message.answer("Напишите комментарий нашему ресторану")


@review_router.callback_query(F.data == '4')
async def badly_us(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(cleanliness_rating='4')
    await state.set_state(RestourantReview.extra_comments)
    await callback.message.answer("Напишите комментарий нашему ресторану")


@review_router.callback_query(F.data == '3')
async def badly_us(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(cleanliness_rating='3')
    await state.set_state(RestourantReview.extra_comments)
    await callback.message.answer("Напишите комментарий нашему ресторану: ")


@review_router.callback_query(F.data == '2')
async def badly_us(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(cleanliness_rating='2')
    await state.set_state(RestourantReview.extra_comments)
    await callback.message.answer("Напишите комментарий нашему ресторану: ")


@review_router.message(RestourantReview.extra_comments)
async def extra_comments_us(message: types.Message, state: FSMContext):
    await state.update_data(extra_comments=message.text)
    await message.answer('Спасибо за отзыв!')
    data = await state.get_data()
    print(data)
    await state.clear()


@review_router.callback_query(F.data == 'review')
async def review_us(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(RestourantReview.name)
    await callback.message.answer('Как вас зовут?')

