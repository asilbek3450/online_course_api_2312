import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
import asyncpg
from handlers import router as main_router

API_TOKEN = '7770700132:AAHK4pqbG7gJ00-8LYUPyuBps-uNZA-_dRQ'
DATABASE_URL = "postgresql://postgres:postgres@localhost/online_course"

async def main():
    logging.basicConfig(level=logging.INFO)
    
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())
    
    # DB ulanish
    db = await asyncpg.connect(DATABASE_URL)
    dp["db"] = db

    # Router qo‘shish
    dp.include_router(main_router)

    # Bot ishga tushurish
    await dp.start_polling(bot)

    # Chiqishda db ni yopish
    await db.close()

if __name__ == "__main__":
    asyncio.run(main())
