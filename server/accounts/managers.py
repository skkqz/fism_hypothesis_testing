from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    """
    Кастомный менеджер для модели пользователя.
    """

    def create_user(self, email, password, **kwargs):

        if not email:
            raise ValueError('Введите пожалуйста электронную почту.')

        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **kwargs):

        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)

        if kwargs.get('is_staff') is not True:
            raise ValueError('Суперпользователь должен иметь статус персонала.')

        if kwargs.get('is_superuser') is not True:
            raise ValueError('Суперпользователь должен иметь is_superuser = True')

        return self.create_user(email, password, **kwargs)
