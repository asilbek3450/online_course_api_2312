from aiogram import Router, types, F
from aiogram.types import Message
from keyboards import category_keyboard, course_keyboard
from database import get_categories, get_courses_by_category_name, get_lessons_by_course_name

router = Router()

@router.message(F.text == "/start")
async def on_start(message: Message):
    markup = await category_keyboard()
    await message.answer("Salom! Qaysi kategoriya qiziqtiradi?", reply_markup=markup)


@router.message(F.text.startswith("📚 "))
async def on_category_handler(message: Message):
    category_title = message.text[2:]
    categories = await get_categories()
    category_id = next((c["id"] for c in categories if c["title"] == category_title), None)

    if not category_id:
        await message.answer("Bunday kategoriya topilmadi.")
        return

    courses = await get_courses_by_category_name(category_title)
    text = "\n".join([f"📖 {c['title']}" for c in courses]) or "Kurslar topilmadi."
    markup = course_keyboard(courses)
    await message.answer(f"**{category_title}** kategoriyasidagi kurslar:\n{text}", reply_markup=markup)


@router.message(F.text.startswith("📖 "))
async def on_course_handler(message: Message):
    course_title = message.text[2:]
    # Agar kerak bo‘lsa, barcha kurslarni olish kerak
    lessons = await get_lessons_by_course_name(course_title)
    text = "\n".join([f"🎥 {l['title']}" for l in lessons]) or "Darslar topilmadi."
    await message.answer(f"**{course_title}** kursidagi darslar:\n{text}")
