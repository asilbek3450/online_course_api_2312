from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

# UserProfile, Course, Lesson, Enrollment

# UserProfile(AbstractUser)-> status(student, teacher), bio, profile_picture, created_at, updated_at
# Course -> nomi, description, price, image, category, created_at, updated_at
# Lesson -> title, content, video_url, course_id, created_at, updated_at
# Enrollment -> user_id, course_id, created_at, updated_at
class UserProfile(AbstractUser):
    STATUS_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='student')
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.URLField()
    age = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    image = models.URLField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='courses')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    video_url = models.URLField()
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Enrollment(models.Model):
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='enrollments')
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user_id.username} enrolled in {self.course_id.title}"
