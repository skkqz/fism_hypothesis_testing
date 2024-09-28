import logging

from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created

from .models import CustomUser, ProfileUser

logger = logging.getLogger(__name__)


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


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    """
    Отправка письма с восстановлением пароля пользователю.
    """

    email_plaintext_message = (f"Привет,\n\nВы запросили сброс пароля. \nЧтобы сбросить пароль,"
                               f" нажмите на следующую ссылку:"
                               f"\nhttp://localhost:8000/reset-password?token={reset_password_token.key}\n"
                               f"\nС наилучшими пожеланиями,,\nВаша команда F#m.")

    send_mail(
        # Title:
        "Сброс пароля {title}".format(title="localohost:8000"),
        # Message:
        email_plaintext_message,
        # From:
        "skkqw@yandex.ru",
        # To:
        [reset_password_token.user.email]
    )

    logger.info(f'Пользователь {reset_password_token.user.email} запросил восстановление пароля.')
