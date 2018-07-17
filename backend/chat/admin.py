from django.contrib import admin

# Register your models here.
from .models import ChatSession, ChatSessionMessage, ChatSessionMember

admin.site.register(ChatSession)
admin.site.register(ChatSessionMessage)
admin.site.register(ChatSessionMember)