from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from database import get_categories, get_courses_by_category_id, get_lessons_by_course_id

async def category_keyboard():
    categories = await get_categories()
    builder = ReplyKeyboardBuilder()
    for category in categories:
        button = KeyboardButton(text=f"📚 {category['title']}")
        builder.add(button)
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)

def course_keyboard(courses):
    builder = ReplyKeyboardBuilder()
    for course in courses:
        button = KeyboardButton(text=f"📖 {course['title']}")
        builder.add(button)
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)

