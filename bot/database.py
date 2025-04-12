import asyncpg
from aiogram import Bot

async def get_categories():
    conn = await asyncpg.connect("postgresql://postgres:postgres@localhost/online_course")
    rows = await conn.fetch("SELECT id, title FROM apps_category")
    await conn.close()
    return [{"id": r["id"], "title": r["title"]} for r in rows]

async def get_courses_by_category_name(category_name):
    conn = await asyncpg.connect("postgresql://postgres:postgres@localhost/online_course")
    if category_name:
        rows = await conn.fetch("SELECT id, title FROM apps_course WHERE category_id_id=(SELECT id FROM apps_category WHERE title=$1)", category_name)
    else:
        rows = await conn.fetch("SELECT id, title FROM apps_course")
    await conn.close()
    return [{"id": r["id"], "title": r["title"]} for r in rows]

async def get_lessons_by_course_name(course_name):
    conn = await asyncpg.connect("postgresql://postgres:postgres@localhost/online_course")
    if course_name:
        rows = await conn.fetch("SELECT id, title FROM apps_lesson WHERE course_id_id=(SELECT id FROM apps_course WHERE title=$1)", course_name)
    else:
        rows = await conn.fetch("SELECT id, title FROM apps_lesson")
    await conn.close()
    return [{"id": r["id"], "title": r["title"]} for r in rows]