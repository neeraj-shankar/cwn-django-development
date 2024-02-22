from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import logging
from app.serializers import StudentSerializer

logger = logging.getLogger("app")


# Signature: @api_view(http_method_names=['GET'])
@api_view(http_method_names=["GET"])
def hello_world(request):
    logger.info(f"I am logger being initated")
    return Response({"message": "Hello Function based view"})

@api_view(http_method_names=["POST"])
def author_view(request):
    

    return Response({'messgae': 'Not ready yet'})
