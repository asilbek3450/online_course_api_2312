from aiogram import Router, types, F
from aiogram.types import Message
from keyboards import category_keyboard, course_keyboard
from database import get_categories, get_courses_by_category_id, get_lessons_by_course_id

router = Router()

@router.message(F.text == "/start")
async def on_start(message: Message):
    categories = await get_categories()
    markup = category_keyboard(categories)
    await message.answer("Salom! Qaysi kategoriya qiziqtiradi?", reply_markup=markup)


@router.message(F.text.startswith("📚 "))
async def on_category_handler(message: Message):
    category_title = message.text[2:]
    categories = await get_categories()
    category_id = next((c["id"] for c in categories if c["title"] == category_title), None)

    if not category_id:
        await message.answer("Bunday kategoriya topilmadi.")
        return

    courses = await get_courses_by_category_id(category_id)
    markup = course_keyboard(courses)
    await message.answer("Tanlangan kategoriya bo‘yicha kurslar:", reply_markup=markup)

@router.message(F.text.startswith("📖 "))
async def on_course_handler(message: Message):
    course_title = message.text[2:]
    # Agar kerak bo‘lsa, barcha kurslarni olish kerak
    courses = await get_courses_by_category_id(None)  # yoki get_courses() bo‘lishi mumkin
    course_id = next((c["id"] for c in courses if c["title"] == course_title), None)

    if not course_id:
        await message.answer("Bunday kurs topilmadi.")
        return

    lessons = await get_lessons_by_course_id(course_id)
    text = "\n".join([f"📘 {l['title']}" for l in lessons]) or "Darslar topilmadi."
    await message.answer(f"<b>{course_title}</b> kursidagi darslar:\n{text}")
