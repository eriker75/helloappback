from django.contrib import admin
from .models import Chat, ChatMember, Message


class ChatMemberInline(admin.TabularInline):
    model = ChatMember
    extra = 0
    autocomplete_fields = ["user"]
    show_change_link = True


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ("name", "type", "description", "is_active")}),
        ("Creator & Last Message", {"fields": ("creator", "last_message")}),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )
    list_display = ("name", "type", "is_active", "creator", "created_at", "updated_at")
    list_filter = ("type", "is_active", "created_at")
    search_fields = ("name", "description", "creator__email")
    ordering = ("-created_at",)
    inlines = [ChatMemberInline]


@admin.register(ChatMember)
class ChatMemberAdmin(admin.ModelAdmin):
    fieldsets = ((None, {"fields": ("chat", "user", "role", "joined_at")}),)
    list_display = ("chat", "user", "role", "joined_at")
    list_filter = ("role", "joined_at")
    search_fields = ("chat__name", "user__email", "user__username")
    ordering = ("-joined_at",)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "chat",
                    "sender",
                    "content",
                    "type",
                    "parent",
                    "draft_content",
                )
            },
        ),
        ("Status", {"fields": ("readed", "deleted")}),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )
    list_display = ("chat", "sender", "type", "readed", "deleted", "created_at")
    list_filter = ("type", "readed", "deleted", "created_at")
    search_fields = ("chat__name", "sender__email", "content")
    ordering = ("-created_at",)
