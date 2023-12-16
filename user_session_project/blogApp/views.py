from django.shortcuts import render
from blogApp.models import BlogPost
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
import logging
from django.http.response import JsonResponse

log = logging.getLogger(__name__)

def create_permission(request):
    content_type = ContentType.objects.get_for_model(BlogPost)
    permission = Permission.objects.create(
        codename = "can_publish",
        name = "Can Publish Posts",
        content_type = content_type
    )

    log.info(f"The Permission Created:")
    message = {
        "message": "The New Permision created"
    }
    return JsonResponse(data=message)
