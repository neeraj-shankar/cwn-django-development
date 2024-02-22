from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from ApiView.serializers import CategorySerializer
from rest_framework import status
from ApiView.models import Category
from utils.logger import setup_logger
from django.http import Http404
from django.db import IntegrityError

log = setup_logger(__name__)


class CategoryList(APIView):
    """
    CategoryList is a DRF APIView that handles CRUD operations for categories.

    Attributes:
        serializer_class (Serializer): The serializer class used for serializing Category objects.

    Methods:
        get(request, format=None): Retrieves a list of posts.
        post(request, format=None): Creates a new post.
        put(request, pk): Updates an existing post.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_serializer(self, *args, **kwargs):
        """
        Return the serializer instance that should be used for validating and
        deserializing input, and for serializing output.
        """
        if self.request.method == "POST":
            # Use a different serializer for POST requests if needed
            return CategorySerializer(*args, **kwargs)
        return super().get_serializer(*args, **kwargs)

    def get(self, request, format=None):
        """
        Get a list of catgeories.

        Args:
            request (Request): The HTTP request.

        Returns:
            Response: A JSON response with a list of serialized posts.
        """
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        """
        Create a new catgeory.

        Args:
            request (Request): The HTTP request containing category data.

        Returns:
            Response: A JSON response with the serialized post if successful, or errors if unsuccessful.
        """

        try:
            log.info(f"Received Category Data: {request.data}")
            serializer = self.get_serializer(data=request.data)
            log.info(f"Validation Successfully Completed for Category data")
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                log.info(f"Saving to category database Successful")
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError as e:
            log.error(f"Error saving to category database: {e}")
            return Response(
                {"error": "Database error"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

class CategoryDetail(APIView):
    """
    CategoryDetail is a DRF APIView that handles CRUD operations for category.

    Attributes:
        serializer_class (Serializer): The serializer class used for serializing Category objects.

    Methods:
        get(request, pk, format=None): Retrieves specific catgeory based on given pk.
        put(request, pk): Updates an existing post.
    """

    def get_object(self, pk):
        try:
            category = Category.objects.get(pk=pk)
            return category
        except Category.DoesNotExist:
            raise Response(
                {"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND
            )

    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = CategorySerializer(post)
        return Response(serializer.data)

    def patch(self, request, pk):
        """
        Update an existing category.

        Args:
            request (Request): The HTTP request containing updated category data.
            pk (int): The primary key of the post to be updated.

        Returns:
            Response: A JSON response with the updated serialized post if successful, or errors if unsuccessful.
        """
        post = self.get_object(pk)
        serializer = CategorySerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





