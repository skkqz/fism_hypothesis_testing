from django.contrib import admin
from unfold.admin import ModelAdmin
from django_rest_passwordreset.models import ResetPasswordToken

from .models import CustomUser, ProfileUser


@admin.register(CustomUser)
class CustomUserAdmin(ModelAdmin):

    list_display = ['email', 'first_name']


@admin.register(ProfileUser)
class ProfileUserAdmin(ModelAdmin):

    list_display = ['user', 'role']


admin.site.unregister(ResetPasswordToken)