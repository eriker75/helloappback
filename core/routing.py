from django.urls import path, include

# Import chat websocket routing
from apps.chats.routing import websocket_urlpatterns as chat_websocket_urlpatterns

websocket_urlpatterns = [
    # Include chat websocket routes
    *chat_websocket_urlpatterns,
]