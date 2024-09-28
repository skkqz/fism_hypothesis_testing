from django.urls import path
from .views import (UserRegistrationView, UserLoginView, UserLogoutView, ProfilesUsersView, ProfileDetailUserView,
                    MeProfileUserView)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profiles/', ProfilesUsersView.as_view(), name='profiles'),
    path('profiles/<uuid:pk>', ProfileDetailUserView.as_view(), name='profiles_detail'),
    path('profiles/me/', MeProfileUserView.as_view(), name='profile_user'),
]
