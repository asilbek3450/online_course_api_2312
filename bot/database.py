from aiogram import types
import asyncpg


async def get_courses():
    conn = await asyncpg.connect(user='postgres', password='postgres', database='online_course', host='localhost')
    courses = await conn.fetch('SELECT * FROM apps_course')
    await conn.close()
    return courses


