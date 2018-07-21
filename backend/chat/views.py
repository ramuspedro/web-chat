from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions

from .models import ChatSession
from .serializers import ChatSessionSerializer

class ChatSessionList(generics.ListCreateAPIView):
  permission_classes = (permissions.IsAuthenticated,)
  queryset = ChatSession.objects.all()
  serializer_class = ChatSessionSerializer