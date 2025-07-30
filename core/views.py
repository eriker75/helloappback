from django.http import JsonResponse
import os
from datetime import datetime

def status_view(request):
    environment = os.environ.get("ENV") or os.environ.get("ENVIRONMENT") or "development"
    return JsonResponse({
        "status": "ok",
        "message": "Backend running",
        "environment": environment,
        "datetime": datetime.utcnow().isoformat() + "Z"
    })