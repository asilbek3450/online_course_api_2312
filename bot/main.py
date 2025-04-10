import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncpg
import asyncio
from database import get_courses
from handlers import on_start, on_category_handler

# Telegram bot tokenini o'rnatish
API_TOKEN = '7770700132:AAHK4pqbG7gJ00-8LYUPyuBps-uNZA-_dRQ'



async def main():
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher(bot)

    @dp.message_handler(commands=['start'])
    async def cmd_start(message: types.Message):
        await on_start(message)

    @dp.message_handler(lambda message: message.text.startswith('📚'))
    async def cat_handler(message: types.Message):
        await on_category_handler(message)

    # Botni ishga tushurish
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling()


if __name__ == '__main__':
    asyncio.run(main())
