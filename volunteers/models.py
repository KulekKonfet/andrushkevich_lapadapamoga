from django.db import models
from django.contrib.auth.models import User

class VolunteerProject(models.Model):
    CATEGORY_CHOICES = [
        ('animals', 'Помощь животным'),
        ('ecology', 'Экология'),
    ]
    
    title = models.CharField(max_length=200, verbose_name="Название проекта")
    description = models.TextField(verbose_name="Описание")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, verbose_name="Категория")
    created_at = models.DateTimeField(auto_now_add=True)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organized_projects')
    participants = models.ManyToManyField(User, related_name='participated_projects', blank=True)
    image = models.ImageField(upload_to='projects/', null=True, blank=True)

    def __str__(self):
        return self.title

class VolunteerProfile(models.Model):
    ROLE_CHOICES = [
    ('organizer', 'Организатор'),
    ('volunteer', 'Волонтёр'),
]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telegram_id = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='volunteer',
        verbose_name="Роль"
    )


    def __str__(self):
        return self.user.username
