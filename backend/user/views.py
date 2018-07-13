# user/views.py

from django.shortcuts import render

# Create your views here.
from django.contrib.auth import get_user_model
from rest_framework import generics

from .serializers import UserSerializer

class UserList(generics.ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer