import os
import keyboards as kb

import texts
from aiogram import Bot, Dispatcher, executor, types


bot = Bot(token=os.getenv("OPORA_MY_TEAM_TOKEN"))
dp = Dispatcher(bot)


@dp.message_handler(command=['start'])
async def welcome_command(message: types.message):
    await message.reply(texts.get_text(filename), reply_markup=kb.inline_link_to_questionnaire_kb)


if __name__ == "__main__":
    filename: str = 'data.json'
    executor.start_polling(dp, skip_updates=True)
