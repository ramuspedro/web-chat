from .models import ChatSession
from rest_framework import serializers

from django.contrib.auth import get_user_model

from user.serializers import UserSerializer

class ChatSessionListSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField()
    owner = serializers.SerializerMethodField()
    class Meta:
        model = ChatSession
        fields = ('__all__')

    def get_owner(self, obj):
        # print(obj.id)
        # print("********************")
        # print(get_user_model().objects.get(username = obj.owner))
        return UserSerializer(get_user_model().objects.get(username = obj.owner)).data
        # return get_user_model().objects.get(username = obj.owner).username

class ChatSessionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatSession
        fields = ('room_name', 'id')