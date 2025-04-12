import asyncpg
from aiogram import Bot

async def get_categories():
    conn = await asyncpg.connect("postgresql://postgres:postgres@localhost/online_course")
    rows = await conn.fetch("SELECT id, title FROM apps_category")
    await conn.close()
    return [{"id": r["id"], "title": r["title"]} for r in rows]

async def get_courses_by_category_id(category_id):
    conn = await asyncpg.connect("postgresql://postgres:postgres@localhost/online_course")
    if category_id:
        rows = await conn.fetch("SELECT id, title FROM apps_course WHERE category_id_id=$1", category_id)
    else:
        rows = await conn.fetch("SELECT id, title FROM apps_category")
    await conn.close()
    return [{"id": r["id"], "title": r["title"]} for r in rows]

async def get_lessons_by_course_id(course_id):
    conn = await asyncpg.connect("postgresql://postgres:postgres@localhost/online_course")
    rows = await conn.fetch("SELECT id, title FROM apps_lesson WHERE course_id_id=$1", course_id)
    await conn.close()
    return [{"id": r["id"], "title": r["title"]} for r in rows]
