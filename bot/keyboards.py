from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def category_keyboard(categories):
    builder = ReplyKeyboardBuilder()
    kb = []
    for category in categories:
        button = KeyboardButton(f"📚 {category['title']}")
        kb.append(button)
    builder.add(*kb)
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)

def course_keyboard(courses):
    builder = ReplyKeyboardBuilder()
    for course in courses:
        button = KeyboardButton(f"📖 {course['title']}")
        builder.add(button)
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)

