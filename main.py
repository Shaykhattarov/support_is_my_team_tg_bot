import os
import keyboards as kb

from texts import welcome_text
from aiogram import Bot, Dispatcher, executor, types


bot = Bot(token=os.getenv("OPORA_MY_TEAM_TOKEN"))
dp = Dispatcher(bot)


@dp.message_handler(command=['start'])
async def information_text(message: types.Message):
    await message.reply(welcome_text, reply_markup=kb.inline_link_to_questionnaire_kb)


if __name__ == "__main__":
    executor.start_polling(dp)
