from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User, Profile

class AuthAndProfileAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="test@example.com",
            username="testuser",
            password="testpass123"
        )
        self.profile = self.user.profile

    def test_register(self):
        url = reverse("auth-register")
        data = {
            "email": "newuser@example.com",
            "username": "newuser",
            "password": "newpass123",
            "password2": "newpass123",
            "first_name": "New",
            "last_name": "User"
        }
        resp = self.client.post(url, data)
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(resp.data["email"], "newuser@example.com")

    def get_tokens(self):
        url = reverse("auth-login")
        resp = self.client.post(url, {"email": "test@example.com", "password": "testpass123"})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        return resp.data["access"], resp.data["refresh"]

    def test_login(self):
        access, refresh = self.get_tokens()
        self.assertTrue(access)
        self.assertTrue(refresh)

    def test_logout(self):
        access, refresh = self.get_tokens()
        url = reverse("auth-logout")
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access}")
        resp = self.client.post(url, {"refresh": refresh})
        self.assertEqual(resp.status_code, status.HTTP_205_RESET_CONTENT)

    def test_password_change(self):
        access, _ = self.get_tokens()
        url = reverse("auth-password-change")
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access}")
        resp = self.client.post(url, {"old_password": "testpass123", "new_password": "changedpass456"})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertIn("detail", resp.data)

    def test_user_me_get(self):
        access, _ = self.get_tokens()
        url = reverse("user-me")
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access}")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data["email"], "test@example.com")

    def test_user_me_patch(self):
        access, _ = self.get_tokens()
        url = reverse("user-me")
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access}")
        resp = self.client.patch(url, {"first_name": "NewName"})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data["first_name"], "NewName")

    def test_profile_me_get(self):
        access, _ = self.get_tokens()
        url = reverse("profile-me")
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access}")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data["user"]["email"], "test@example.com")

    def test_profile_me_patch(self):
        access, _ = self.get_tokens()
        url = reverse("profile-me")
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access}")
        resp = self.client.patch(url, {"bio": "Hello world!"})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data["bio"], "Hello world!")
