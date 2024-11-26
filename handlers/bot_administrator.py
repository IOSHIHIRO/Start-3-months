from aiogram import F,Router,types
from aiogram.fsm.state import State, StatesGroup,default_state
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command

from bot_cod import database

bot_administrator_router = Router()
bot_administrator_router.message.filter(
    F.from_user.id == 1627653043
)
bot_administrator_router.callback_query.filter(
    F.from_user.id == 1627653043
)

class Admin(StatesGroup):
    name = State()
    price = State()
    category = State()

class Category(StatesGroup):
    name = State()

@bot_administrator_router.message(Command("newcategory"))
async def create_new_category(message: types.Message, state: FSMContext):
    await state.set_state(Category.name)
    await message.answer("Задайте категорию блюда:")

@bot_administrator_router.message(Category.name)
async def process_name(message: types.Message, state: FSMContext):
    new_categories = message.text
    database.execute(
    query="""
        INSERT INTO dish_categories(name) VALUES(?)
    """,
        params=(new_categories,)
    )
    await message.answer("Категория добавлен")
    await state.clear()


@bot_administrator_router.message(Command("dish"), default_state)
async def create_dish(message: types.Message, state: FSMContext):
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
    all_categories = database.fetch("SELECT * FROM dish_categories")
    if not all_categories:
        await message.answer("Нет категории")
        state.clear()
        return
    kd = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text=category["name"]) for category in all_categories]
        ]
    )
    await state.set_state(Admin.category)
    await message.answer('Задайте категорию:', reply_markup=kd)

@bot_administrator_router.message(Admin.category)
async def create_dish(message: types.Message, state: FSMContext):
    print(message.text)
    category = database.fetch(
        query="SELECT * FROM dish_categories WHERE name = ?",
        params=(message.text,)
    )
    if not category:
        await message.answer("Вы напечатали неуществующий в базе данных категория")
        return
    await state.update_data(category=category[0]["id"])

    data = await state.get_data()
    database.execute(
        query="""
        INSERT INTO dishes(name, price, category_id) VALUES (?,?,?)
        """,
        params=(data['name'], data['price'], data['category']),
    )
    await state.clear()
    await message.answer('Блюдо добавлено')

