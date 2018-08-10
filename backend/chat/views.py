from notifications.signals import notify

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

    # get chat session
    chat_session = ChatSession.objects.get(uri = uri)
    chat_session_serialized = ChatSessionListSerializer(chat_session).data

    # get the mensagens from a chat session
    chat_session_messages = chat_session.messages.all()
    chat_session_messages_serialized = ChatSessionMessageSerializer(list(chat_session_messages), many=True).data

    # add username to identify the mensagens
    for key in range(len(list(chat_session_messages))):
      chat_session_messages_serialized[key]['username'] = str(chat_session_messages[key].user)
      
    return Response({
      'chat_session': chat_session_serialized,
      'messages': chat_session_messages_serialized
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

class ChatSessionMessageCreate(generics.CreateAPIView):
  permission_classes = (permissions.IsAuthenticated,)
  serializer_class = ChatSessionMessageSerializer
  # queryset = ChatSessionMessage.objects.all()

  def post(self, request, *args, **kwargs):
    """POST create a chat message using a chat_id"""
    # create a chat message

    # chat_session_message = ChatSessionMessage.objects.create(
    #   message = request.data['message'],
    #   user = request.user,
    #   chat_session = ChatSession.objects.get(id = request.data['chat_session'])
    # )
    # chat_session_message_serialized = ChatSessionMessageSerializer(chat_session_message)
    # info = chat_session_message_serialized.data
    # info['username'] = str(chat_session_message.user)

    print(request.data)

    notif_args = {
      'source': request.user,
      'source_display_name': "TESTEEEEEEEEEE",
      'category': 'chat', 'action': 'Sent',
      'obj': "TESTEEEEEEEEEE",
      'short_description': 'You a new message', 'silent': True,
      'extra_data': {'uri': "auhuahuahussijisjijs"}
    }
    notify.send(
        sender=self.__class__, **notif_args, channels=['websocket']
    )

    # send to rabbitmq
    return Response({})
    # return Response(info)

class ChatSessionMessageList(generics.ListAPIView):
  permission_classes = (permissions.IsAuthenticated,)
  serializer_class = ChatSessionMessageSerializer
  queryset = ChatSessionMessage.objects.all()

class ChatSessionMessageListDetail(generics.RetrieveAPIView):
  permission_classes = (permissions.IsAuthenticated,)
  serializer_class = ChatSessionMessageSerializer
  # queryset = ChatSessionMessage.objects.all()
  def get(self, request, *args, **kwargs):
    """Get chat by id"""
    pk = kwargs['pk']
    # get chat session
    chat_session_message = ChatSessionMessage.objects.get(id = pk)
    chat_session_message_serialized = ChatSessionMessageSerializer(chat_session_message)
    print(chat_session_message_serialized.data)
    info = chat_session_message_serialized.data
    info['username'] = str(chat_session_message.user)
    return Response(info)