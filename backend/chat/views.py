from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from rest_framework.response import Response

from .models import ChatSession, ChatSessionMember
from .serializers import ChatSessionListSerializer, ChatSessionCreateSerializer

class ChatSessionList(generics.ListAPIView):
  permission_classes = (permissions.IsAuthenticated,)
  queryset = ChatSession.objects.all()
  serializer_class = ChatSessionListSerializer
  # def get(self, request):
  #   serializer = ChatSessionListSerializer(ChatSession.objects.all())
  #   print(serializer)
  #   return Response(serializer.data)

class ChatSessionCreate(generics.CreateAPIView):
  permission_classes = (permissions.IsAuthenticated,)
  serializer_class = ChatSessionCreateSerializer
  # queryset = ChatSession.objects.all()
  def post(self, request, *args, **kwargs):

    # user create the chat session
    user = request.user
    chat_session = ChatSession.objects.create(owner = user, room_name = request.data['room_name'])
    serializer_class = ChatSessionCreateSerializer(chat_session)

    # user already is a member
    ChatSessionMember.objects.create(user = user, chat_session = chat_session)

    # print(serializer_class.data)
    return Response(serializer_class.data)
