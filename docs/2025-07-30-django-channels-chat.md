# 2025-07-30 – Integrate Django Channels for Real-Time Chat

## Objective

Enable real-time chat using Django Channels and websockets, while preserving HTTP endpoints for chat/message retrieval (with pagination). The system must allow:
- HTTP GET for all chats of a logged-in user.
- HTTP GET (paginated) for messages in a chat.
- Websocket listening for new chats or messages.

## Action Plan

1. Add `channels` and `channels_redis` to requirements.
2. Update `docker/docker-compose.dev.yml` and `docker/docker-compose.prod.yml` to include a Redis service for Channels.
3. Update Django settings:
   - Add `channels` to `INSTALLED_APPS`.
   - Configure `ASGI_APPLICATION` and `CHANNEL_LAYERS`.
4. Update `core/asgi.py` for Channels.
5. Create `apps/chats/consumers.py` and `apps/chats/routing.py` for websocket consumers and routing.
6. Update `core/urls.py` and add `core/routing.py` for websocket routing.
7. Ensure HTTP endpoints for chat/message retrieval remain functional.
8. Document all changes in `docs/devlog.md` and update `README.md` if necessary.

## Files to Modify/Create

- requirements.txt
- docker/docker-compose.dev.yml
- docker/docker-compose.prod.yml
- core/settings/base.py
- core/asgi.py
- core/routing.py (new)
- apps/chats/consumers.py (new)
- apps/chats/routing.py (new)
- docs/devlog.md
- README.md (if needed)

## Observations

- Redis will be used as the channel layer backend.
- All changes will be documented and tested for both HTTP and websocket functionality.