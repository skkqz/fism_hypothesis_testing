import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    """
    Кастомная моодель пользователя.
    """

    username = None

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, verbose_name='Электронная почта')
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=30, blank=True, null=True, verbose_name='Фамилия')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email


class ProfileUser(models.Model):
    """
    Модель профиля пользователя.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile', verbose_name='Профиль')
    avatar = models.ImageField(upload_to='avatars/', blank=True, verbose_name='Аватар')
    bio = models.TextField(max_length=500, blank=True, verbose_name='О себе')
    is_analyst = models.BooleanField(default=False, verbose_name='Аналитик')
    is_super_analyst = models.BooleanField(default=False, verbose_name='Супер Аналитик')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

    def __str__(self):
        return self.user.first_name
