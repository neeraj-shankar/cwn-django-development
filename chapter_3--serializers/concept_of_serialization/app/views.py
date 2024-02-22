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
def student_view(request):
    client_data = request.data 
    logger.info(f"Received Payload: {client_data}")
    logger.info(f"Client Data Type: {type(client_data)}") # Client Data Type: <class 'dict'>

    # Using Serializer to convert client data
    serializer = StudentSerializer(data=client_data)
    if serializer.is_valid(raise_exception=True):
        logger.info(f"Serialized Data: {serializer.data}")
        logger.info(f"Serialized Data Type: {type(serializer.data)}") 
        # Serialized Data Type: <class 'rest_framework.utils.serializer_helpers.ReturnDict'>

    return Response({'messgae': 'Not ready yet'})
