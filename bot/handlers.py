from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncpg
import asyncio
from aiogram import types
from database import get_courses, get_categories


async def on_start(message: types.Message):
    categories = await get_categories()
    category_buttons = ReplyKeyboardMarkup(resize_keyboard=True)
    for category in categories:
        button = KeyboardButton(f'📚 {category['title']}')
        category_buttons.add(button)
    await message.answer("Salom! Sizga qaysi kategoriya qiziqadi?", reply_markup=category_buttons)
    await message.answer("Iltimos, kategoriya tanlang:")


async def on_category_handler(message: types.Message):
    user_category = message.text[2:]
    categories = await get_categories()
    for c in categories:
        if user_category == c['title']:
            category_id = c['id']
            break
        else:
            await message.answer("Bunday kategoriya mavjud emas. Iltimos, boshqa kategoriya tanlang.")
            return
    await message.answer(f"Tanlangan kategoriya: {user_category}")
    courses = await get_courses(category_id)
    course_buttons = ReplyKeyboardMarkup(resize_keyboard=True)
    for course in courses:
        button = KeyboardButton(f'📖 {course['title']}')
        course_buttons.add(button)
    await message.answer("Tanlangan kategoriya bo'yicha kurslar:", reply_markup=course_buttons)
    await message.answer("Iltimos, kurs tanlang:")