import logging

from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model, authenticate, login
from rest_framework import serializers

from .models import CustomUser, ProfileUser
from .utils import update_profile_avatar

logger = logging.getLogger(__name__)

User = get_user_model()


class RegisterUserSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для регистрации пользователя.
    """

    password_1 = serializers.CharField(max_length=128, label='Введите пароль', write_only=True,
                                       validators=[validate_password], style={'input_type': 'password'})
    password_2 = serializers.CharField(max_length=128, label='Повторите пароль', write_only=True,
                                       validators=[validate_password], style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('email', 'password_1', 'password_2', 'first_name')

    def validate(self, attrs):

        if attrs['password_1'] != attrs['password_2']:
            raise serializers.ValidationError({'message': 'Пароль не совпадает.'})
        return attrs


    def create(self, validated_data):

        user = CustomUser(
            email=validated_data['email'],
            first_name=validated_data['first_name']
        )
        user.set_password(validated_data['password_1'])
        user.save()

        return user


class LoginUserSerializer(serializers.Serializer):
    """
    Сериалайзер для аутентификации пользователя.
    """

    email = serializers.EmailField(label='Email')
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    def create(self, attrs):

        user = authenticate(email=attrs['email'], password=attrs['password'])
        if user is None:
            raise serializers.ValidationError({'message': 'Неверные учетные данные.'})

        login(self.context['request'], user)
        logger.info(f'Пользователь {user} успешно авторизовался.')

        return user


class ProfileUserSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для профиля пользователя.
    """

    avatar = serializers.ImageField(use_url=False)

    class Meta:
        model = ProfileUser
        fields = ('avatar', 'role', 'last_login', 'created_at')
        read_only_fields  = ('role', 'last_login', 'crate_at', )


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Сериалайзер кастомного пользователя.
    """

    profile = ProfileUserSerializer()

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'profile')


class MeUserProfileSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для детального отображения профиля и его изменений.
    """

    profile = ProfileUserSerializer()

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'profile')


    def create(self, validated_data):
        raise NotImplemented('Данный метод не разрешен.')


    def update(self, instance, validated_data):

        profile_avatar = validated_data.pop('profile')
        if profile_avatar:
            update_profile_avatar(instance_profile=instance.profile, profile_avatar=profile_avatar)

        return super().update(instance, validated_data)
