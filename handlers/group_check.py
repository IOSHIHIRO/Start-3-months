from datetime import timedelta
from aiogram import Router,F,types


grou_check_router = Router()

BAD_WORDS = ("дурак",)



@grou_check_router.message(F.text)
async def group_check(message: types.Message):
    for bad_word in BAD_WORDS:
        if bad_word in message.text.lower():
            await message.answer("Сам такой")
            await message.delete()
            break
        if message.reply_to_message:
            user = message.reply_to_message.from_user
            await message.chat.ban(
                user_id = user.id,
                until_date=timedelta(minutes=10)
            )
            await message.answer("Вы были забанины")

@grou_check_router.message(F.photo)
async def delete_check(message: types.Message):
    await message.delete()
    await message.answer("Нельзя картики и гифки")