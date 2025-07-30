from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Profile, SocialAccount


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("username", "first_name", "last_name")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "username", "password1", "password_confirmed"),
            },
        ),
    )
    list_display = (
        "email",
        "username",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
        "date_joined",
    )
    list_filter = ("is_staff", "is_superuser", "is_active", "date_joined")
    search_fields = ("email", "username", "first_name", "last_name")
    ordering = ("-date_joined",)
    filter_horizontal = ("groups", "user_permissions")


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ("user", "alias", "avatar", "bio")}),
        (
            "Personal info",
            {
                "fields": (
                    "birth_date",
                    "gender",
                    "interested_in",
                    "address",
                    "location",
                    "latitude",
                    "longitude",
                )
            },
        ),
        (
            "Status",
            {"fields": ("is_onboarded", "status", "is_verified", "last_online")},
        ),
        ("Preferences", {"fields": ("preferences",)}),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )
    list_display = (
        "user",
        "alias",
        "is_verified",
        "status",
        "is_onboarded",
        "last_online",
    )
    list_filter = ("is_verified", "status", "is_onboarded", "gender")
    search_fields = ("user__email", "alias", "bio", "address", "location")
    ordering = ("-created_at",)


@admin.register(SocialAccount)
class SocialAccountAdmin(admin.ModelAdmin):
    list_display = ("user", "provider", "uid")
    list_filter = ("provider",)
    search_fields = ("user__email", "provider", "uid")
    ordering = ("provider", "user")
