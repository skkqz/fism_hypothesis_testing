import os
from typing import Dict

from PIL import Image
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.core.files.uploadedfile import InMemoryUploadedFile


import os
from django.utils.crypto import get_random_string
from PIL import Image

from django.conf import settings


def rename_image(name_image: str) -> str:

    """
    Изменение название изображения.
    :param name_image: Имя файла.
    :return: Изменённое имя файла.
    """

    root, ext = os.path.splitext(name_image)
    new_name = f'avatars/{get_random_string(length=20)}{ext}'

    return new_name


def resize_image(image):

    """
    Изменение размера изображение.
    :param image: Изображение
    :return: Изображение с изменённым размером 200px 200px
    """

    img = Image.open(image)
    img.thumbnail((200, 200))
    new_name = rename_image(image.name)
    path_image = f'{settings.MEDIA_ROOT}/{new_name}'
    print(path_image)
    img.save(path_image)

    return new_name


def update_profile_avatar(instance_profile, profile_avatar: Dict[str, InMemoryUploadedFile]):
    """
    Обновление аватара у пользователя.
    :param instance_profile: Профиль пользователя.
    :param profile_avatar: Словарь с данными аватара.
    :return:
    """

    image = resize_image(profile_avatar['avatar'])
    instance_profile.avatar.save(image, ContentFile(profile_avatar['avatar'].read()), save=True)
    # instance_profile.avatar = image
    # instance_profile.save()

