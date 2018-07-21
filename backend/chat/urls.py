from django.urls import path

from .views import ChatSessionList

urlpatterns = [
    path('chat-session/', ChatSessionList.as_view()),
]