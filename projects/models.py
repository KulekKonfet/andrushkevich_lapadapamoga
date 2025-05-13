from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class VolunteerProject(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)  # Связь с пользователем-организатором
    category = models.CharField(max_length=255, blank=True)  # Категория проекта
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания проекта
    updated_at = models.DateTimeField(auto_now=True)  # Дата последнего обновления проекта

    def __str__(self):
        return self.title
