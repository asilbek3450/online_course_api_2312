from aiogram import types
import asyncpg
conn = asyncpg.connect(user='postgres', password='postgres', database='online_course', host='localhost')

async def get_categories():
    courses = await conn.fetch('SELECT * FROM apps_category')
    await conn.close()
    return courses


async def get_courses(c_id):
    courses = await conn.fetch('SELECT * FROM apps_course WHERE category_id = $1', c_id)
    await conn.close()
    return courses


