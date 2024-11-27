from datetime import timedelta
from aiogram.filters import Command

from aiogram import Router,F,types


grou_check_router = Router()

BAD_WORDS = ("дурак",)

@grou_check_router.message(Command("ban"))
async def ban(message: types.Message):
    if not message.reply_to_message:
        await message.answer("Надо сделать реплэй")
    else:
        id = message.reply_to_message.from_user.id
        await message.bot.ban_chat_member(chat_id=message.chat.id, user_id=id,
                                          until_date=timedelta(seconds=30,minutes=5,days=1))

@grou_check_router.message(F.text)
async def group_check(message: types.Message):
    for bad_word in BAD_WORDS:
        if bad_word in message.text.lower():
            await message.answer("Вы были забанины за плохое поведение ")
            await message.bot.ban_chat_member(chat_id=message.chat.id,
                                              user_id=message.from_user.id,
                                              until_date=timedelta(seconds=10))
            await message.delete()


@grou_check_router.message(F.photo)
async def delete_check(message: types.Message):
    await message.delete()
    await message.answer("Нельзя картики и гифки")