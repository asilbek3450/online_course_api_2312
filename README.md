# 🎓 Online Course API

Online Course — bu o‘quv platformasi uchun ishlab chiqilgan Django REST API. Foydalanuvchilar (talabalar va o‘qituvchilar), kurslar, darslar va ro‘yxatdan o‘tish (enrollment) funksiyalarini o‘z ichiga oladi.

## 🛠 Texnologiyalar

- Python 3.x
- Django
- Django REST Framework
- drf-yasg (Swagger dokumentatsiya uchun)
- SQLite (yoki siz xohlagan boshqa DB)

## 📁 Strukturasi

- `UserProfile` — foydalanuvchi (student / teacher)
- `Category` — kurs kategoriyalari
- `Course` — kurslar
- `Lesson` — kurs ichidagi darslar
- `Enrollment` — foydalanuvchi kursga ro‘yxatdan o‘tganligi

## 🚀 O'rnatish

```bash
# 1. Loyihani klonlash
git clone https://github.com/username/medcontrol-api.git
cd medcontrol-api

# 2. Virtual environment yaratish va faollashtirish
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Kerakli kutubxonalarni o‘rnatish
pip install -r requirements.txt

# 4. Migratsiyalar
python manage.py migrate

# 5. Superuser yaratish (ixtiyoriy)
python manage.py createsuperuser

# 6. Serverni ishga tushirish
python manage.py runserver
