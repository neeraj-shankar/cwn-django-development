from django.shortcuts import render
from user_management.serializers import CustomTokenObtainPairSerializer

# Create your views here.
from rest_framework_simplejwt.views import TokenObtainPairView

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
