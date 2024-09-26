from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import CustomUser, ProfileUser



@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Сигналы для создания профиля пользователя
    """

    if created:
        ProfileUser.objects.create(user=instance)


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    """
    Сигналы для сохранения профиля пользователя
    """

    instance.profile.save()
