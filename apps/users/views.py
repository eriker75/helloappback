from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
import google.auth.transport.requests
import google.oauth2.id_token
from .models import User, Profile, SocialAccount
from .serializers import (
    UserSerializer,
    ProfileSerializer,
    RegisterSerializer,
    PasswordChangeSerializer,
)


class UserMeView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class ProfileMeView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.profile


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = [permissions.AllowAny]


class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class PasswordChangeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = PasswordChangeSerializer(data=request.data)
        user = request.user
        if serializer.is_valid():
            if not user.check_password(serializer.validated_data["old_password"]):
                return Response(
                    {"old_password": "Wrong password."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            user.set_password(serializer.validated_data["new_password"])
            user.save()
            return Response({"detail": "Password changed successfully."})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GoogleLoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        id_token = request.data.get("id_token")
        if not id_token:
            return Response(
                {"detail": "Missing id_token"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # Verify token with Google
            request_adapter = google.auth.transport.requests.Request()
            idinfo = google.oauth2.id_token.verify_oauth2_token(
                id_token, request_adapter
            )
            # idinfo contains: sub, email, name, picture, etc.
            google_sub = idinfo["sub"]
            email = idinfo.get("email")
            name = idinfo.get("name", "")
            picture = idinfo.get("picture", "")

            User = get_user_model()
            try:
                social = SocialAccount.objects.get(provider="google", uid=google_sub)
                user = social.user
            except SocialAccount.DoesNotExist:
                # If user with this email exists, link it; else create new user
                user, created = User.objects.get_or_create(
                    email=email,
                    defaults={
                        "username": email.split("@")[0],
                        "first_name": name.split(" ")[0] if name else "",
                        "last_name": (
                            " ".join(name.split(" ")[1:])
                            if name and len(name.split(" ")) > 1
                            else ""
                        ),
                        "is_active": True,
                    },
                )
                # Create SocialAccount
                SocialAccount.objects.create(
                    user=user,
                    provider="google",
                    uid=google_sub,
                    extra_data=idinfo,
                )
                # Profile is auto-created by signal

                # Optionally update avatar, etc.
                profile = getattr(user, "profile", None)
                if profile and picture:
                    profile.avatar = picture
                    profile.is_verified = True
                    profile.save()

            # Issue JWT tokens
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                }
            )
        except Exception as e:
            return Response(
                {"detail": f"Google login failed: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )
