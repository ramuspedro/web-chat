from .models import ChatSession
from rest_framework import serializers

class ChatSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatSession
        fields = ('__all__')
