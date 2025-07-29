from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Chat(models.Model):
    CHAT_TYPE_CHOICES = (
        ("private", "Private"),
        ("group", "Group"),
    )
    id = models.UUIDField(primary_key=True, default=models.UUIDField, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    type = models.CharField(max_length=20, choices=CHAT_TYPE_CHOICES, default="private")
    last_message = models.OneToOneField(
        "Message",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="last_in_chat",
    )
    description = models.TextField(blank=True, null=True)
    creator = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="created_chats"
    )
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name or f"Chat {self.id}"


class ChatMember(models.Model):
    ROLE_CHOICES = (
        ("admin", "Admin"),
        ("member", "Member"),
    )
    id = models.UUIDField(primary_key=True, default=models.UUIDField, editable=False)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name="members")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="chat_memberships"
    )
    joined_at = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="member")

    class Meta:
        unique_together = ("chat", "user")

    def __str__(self):
        return f"{self.user.username} in {self.chat}"


class Message(models.Model):
    id = models.UUIDField(primary_key=True, default=models.UUIDField, editable=False)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name="messages")
    sender = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="sent_messages"
    )
    parent = models.ForeignKey(
        "self", on_delete=models.SET_NULL, null=True, blank=True, related_name="replies"
    )
    content = models.TextField(blank=True, null=True)
    draft_content = models.CharField(max_length=500, blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    readed = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Message {self.id} in {self.chat}"
