# user/serilizers.py

from django.contrib.auth import get_user_model
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'username', 'email')
        model = get_user_model()