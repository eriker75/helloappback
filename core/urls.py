from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from core.views import status_view

urlpatterns = [
    path("", status_view, name="status"),
    path("admin/", admin.site.urls),
]
# Authentication and user/profile API endpoints
urlpatterns += [
    # Manual auth endpoints will be added here
    path("api/user/", include("apps.userprofile.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
