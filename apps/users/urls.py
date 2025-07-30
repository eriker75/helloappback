from django.urls import path
from .views import (
    UserMeView,
    ProfileMeView,
    RegisterView,
    CustomTokenObtainPairView,
    LogoutView,
    PasswordChangeView,
    GoogleLoginView,
)

urlpatterns = [
    # Auth endpoints
    path("auth/register/", RegisterView.as_view(), name="auth-register"),
    path("auth/login/", CustomTokenObtainPairView.as_view(), name="auth-login"),
    path("auth/logout/", LogoutView.as_view(), name="auth-logout"),
    path(
        "auth/password/change/",
        PasswordChangeView.as_view(),
        name="auth-password-change",
    ),
    path("auth/google/", GoogleLoginView.as_view(), name="auth-google"),
    # User/profile endpoints
    path("me/", UserMeView.as_view(), name="user-me"),
    path("profile/", ProfileMeView.as_view(), name="profile-me"),
]
