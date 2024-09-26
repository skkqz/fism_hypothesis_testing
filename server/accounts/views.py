from django.contrib.auth import get_user_model, logout

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.views import status

from .serializer import RegisterUserSerializer, LoginUserSerializer, ProfileUserSerializer, CustomUserSerializer
from .models import ProfileUser


User = get_user_model()


class UserRegistrationView(CreateAPIView):
    """
    Представление для регистрации пользователя.
    """

    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer
    permission_classes = [AllowAny]


class UserLoginView(CreateAPIView):
    """
    Представление для авторизации пользователя.
    """

    queryset = User.objects.all()
    serializer_class = LoginUserSerializer
    permission_classes = [AllowAny]


class UserLogoutView(APIView):
    """
    Представление для выхода из аккаунта.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        logout(request)
        return Response({'message': 'Успешный выход.'}, status=status.HTTP_200_OK)


class ProfileUserView(ListAPIView):
    """
    Представление для отображения профилей пользователей.
    """

    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]
