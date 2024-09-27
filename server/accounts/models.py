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

    choice_analysts = (
        ('ANALYST', 'Аналитик'),
        ('SUPER_ANALYST', 'Админ аналитик'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile', verbose_name='Профиль')
    avatar = models.ImageField(upload_to='avatars/', blank=True, verbose_name='Аватар')
    role = models.CharField(max_length=50, default='ANALYST', choices=choice_analysts)
    last_login = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='Дата и время последнего входа')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

    def __str__(self):
        return self.user.first_name
