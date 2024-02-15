from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from ApiView.serializers import AuthorSerializer
from rest_framework import status
from ApiView.models import Author
from utils.logger import setup_logger
from django.http import Http404

log = setup_logger(__name__)


class AuthorList(APIView):
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


class AuthorDetail(APIView):
    """
    Retrieve, update or delete author instances
    """

    def get_author(self, pk):
        try:
            Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        author = self.get_author(pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

    def put(self, request, pk):
        author = self.get_author(pk)
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
