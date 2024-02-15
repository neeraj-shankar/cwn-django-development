from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView
from .models import Author
from .serializers import AuthorSerializer

class AuthorListView(ListCreateAPIView):

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorRetrieveView(RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorUpdateView(UpdateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorDestroyView(DestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

