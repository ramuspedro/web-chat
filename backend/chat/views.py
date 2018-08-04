from django.shortcuts import render
from django.core import serializers

# Create your views here.
from rest_framework import generics, permissions
from rest_framework.response import Response

from .models import ChatSession, ChatSessionMember, ChatSessionMessage
from .serializers import ChatSessionListSerializer, ChatSessionCreateSerializer, ChatSessionMessageSerializer

class ChatSessionList(generics.ListAPIView):
  permission_classes = (permissions.IsAuthenticated,)
  queryset = ChatSession.objects.all()
  serializer_class = ChatSessionListSerializer
  # def get(self, request):
  #   serializer = ChatSessionListSerializer(ChatSession.objects.all())
  #   print(serializer)
  #   return Response(serializer.data)

class ChatSessionListDetail(generics.RetrieveAPIView):
  permission_classes = (permissions.IsAuthenticated,)
  queryset = ChatSession.objects.all()
  serializer_class = ChatSessionListSerializer
  serializer_messages = ChatSessionMessageSerializer

  def get(self, request, *args, **kwargs):
    """Get chat by uri"""
    uri = kwargs['uri']
    # try:
    #   # find chat session
    #   chat_session = ChatSession.objects.get(uri = uri)
    #   serializer_class = ChatSessionListSerializer(chat_session)
    #   # find chat messages
    #   print(serializer_class.data)
    #   chat_session_messages = ChatSessionMessage.objects.get(chat_session = serializer_class.data['id'])
    #   print(chat_session_messages)
    #   return Response(serializer_class.data)
    # except :
    #   return Response({
    #     "detail": "Not found."
    #   })
    # find chat session
    chat_session = ChatSession.objects.get(uri = uri)
    serializer_class = ChatSessionListSerializer(chat_session)
    # find chat messages
    chat_session_messages = ChatSessionMessage.objects.filter(chat_session = serializer_class.data['id'])
    #serializer_messages = ChatSessionMessageSerializer(list(chat_session_messages))

    # print(list(ChatSessionMessage.objects.filter(chat_session = serializer_class.data['id'])))

    messages = []
    for chat_message in list(chat_session_messages):
      #print(ChatSessionMessageSerializer(chat_message).data)
      messages.append(ChatSessionMessageSerializer(chat_message).data)
    #print(chat_message)
    return Response({
      'chat_session': serializer_class.data,
      'messages': messages
    })

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

class ChatSessionMessageCreate(generics.ListCreateAPIView):
  permission_classes = (permissions.IsAuthenticated,)
  serializer_class = ChatSessionMessageSerializer
  queryset = ChatSessionMessage.objects.all()

  # def get(self, request, *args, **kwargs):
  #   chat_session_message = ChatSessionMessage.objects.create(
  #     user = request.user,
  #     chat_session = request.data.chat_session,
  #     message = request.data.message
  #   )

  #   serializer_class = ChatSessionMessageSerializer(chat_session_message)

  #   return Response(serializer_class.data)

  # def post(self, request, *args, **kwargs):
  #   print("**************************")
  #   print(request.user)
  #   chat_session_message = ChatSessionMessage.objects.create(
  #     user = request.user,
  #     chat_session = request.data.chat_session,
  #     message = request.data.message
  #   )

  #   serializer_class = ChatSessionMessageSerializer(chat_session_message)

  #   return Response(serializer_class.data)

class ChatSessionMessageList(generics.ListAPIView):
  permission_classes = (permissions.IsAuthenticated,)
  serializer_class = ChatSessionMessageSerializer
  queryset = ChatSessionMessage.objects.all()
