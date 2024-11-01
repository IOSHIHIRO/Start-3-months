import asyncio
import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import dotenv_values


token = dotenv_values(".env")["BOT_TOKEN"]
names = ['Люси','Майн','Хюрезен']
bot = Bot(token=token)
dp = Dispatcher()
user_id = set()

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    nam_id = message.from_user.id
    user_id.add(nam_id)
    count_id = len(user_id)
    name = message.from_user.first_name
    msg = f"Привет, {name} наш бот обслуживает уже {count_id} пользователя"
    await message.answer(msg)

@dp.message(Command('myinfo'))
async def myinfo_handler(message: types.Message):
    name_id = message.from_user.id
    name = message.from_user.first_name
    name1 = message.from_user.last_name
    first_name = message.from_user.username
    msg = f'Ваш id: {name_id}, имя: {first_name}, фамилия: {name1}, ник: {name}.'
    await message.answer(msg)

@dp.message(Command('random'))
async def random_handler(message: types.Message):
    random_name = random.choice(names)
    await message.answer(f'Рандомное имя из списка {random_name}')

@dp.message(Command('siteyoutube'))
async def youtube_handler(message: types.Message):
    video_url = 'https://www.youtube.com/playlist?list=PL0lO_mIqDDFUev1gp9yEwmwcy8SicqKbt'
    await message.answer(f'Ссылка на видео: {video_url}')


@dp.message()
async def echo_handler(message: types.Message):
    name = message.from_user.first_name
    await message.answer(f'Нет такой команды! Пользователь {name} '
                         f' Выберите команду /start, /myinfo, /random, /siteyoutube ')



async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
