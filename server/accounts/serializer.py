from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model, authenticate, login
from rest_framework import serializers

from .models import CustomUser, ProfileUser

User = get_user_model()


class RegisterUserSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для регистрации пользователя.
    """

    password_1 = serializers.CharField(max_length=128, label='Введите пароль', write_only=True,
                                       validators=[validate_password])
    password_2 = serializers.CharField(max_length=128, label='Повторите пароль', write_only=True,
                                       validators=[validate_password])

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
    password = serializers.CharField(write_only=True)

    def create(self, attrs):

        user = authenticate(email=attrs['email'], password=attrs['password'])

        if user is None:
            raise serializers.ValidationError({'message': 'Неверные учетные данные.'})
        login(self.context['request'], user)
        return user


class ProfileUserSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для профиля пользователя.
    """

    class Meta:
        model = ProfileUser
        fields = ('user', 'bio', 'avatar', 'is_analyst', 'created_at')


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Сериалайзер кастомного пользователя.
    """

    profile = ProfileUserSerializer()

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'profile')