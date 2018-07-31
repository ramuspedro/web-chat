from django.urls import path

from .views import ChatSessionList, ChatSessionListDetail, ChatSessionCreate

urlpatterns = [
    path('chat-session-list/', ChatSessionList.as_view()),
    path('chat-session-list/<uri>/', ChatSessionListDetail.as_view()),
    path('chat-session-create/', ChatSessionCreate.as_view()),
]