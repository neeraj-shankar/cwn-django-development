from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from ApiView.serializers import AuthorSerializer
from rest_framework import status
from ApiView.models import Author
from utils.logger import setup_logger

log = setup_logger(__name__)

class AuthorView(APIView):

    def get(self, request):
        queryset = Author.objects.all()
        serializer = AuthorSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        log.info(f"Received Payload: {request.data}")
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def patch(self, request, *args):
    #     key = request.data["id"]
    #     log.info(f"Requested ID: {key}")
    #     try:
    #         queryset = Category.objects.get(id=key)
    #     except Category.DoesNotExist:
    #         message = {
    #             "message": "The Requested Resource Not Found."
    #         }
    #         return Response(message, status=status.HTTP_404_NOT_FOUND)
        
    #     serializer = CategorySerializer(queryset, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()

    #         return Response(serializer.data)
    #     return Response(serializer.errors)




