import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncpg
import asyncio
from bot.database import get_courses

# Telegram bot tokenini o'rnatish
API_TOKEN = '7770700132:AAHK4pqbG7gJ00-8LYUPyuBps-uNZA-_dRQ'


async def on_start(message: types.Message):
    courses = await get_courses()
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    for course in courses:
        course_name = course['title']
        button = KeyboardButton(course_name)
        keyboard.add(button)

    await message.answer("Kursni tanlang:", reply_markup=keyboard)


async def main():
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher(bot)

    @dp.message_handler(commands=['start'])
    async def cmd_start(message: types.Message):
        await on_start(message)

    # Botni ishga tushurish
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling()


if __name__ == '__main__':
    asyncio.run(main())
