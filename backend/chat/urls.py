from django.urls import path

from .views import ChatSessionList, ChatSessionListDetail, ChatSessionCreate, ChatSessionMessageCreate, ChatSessionMessageList

urlpatterns = [
    path('chat-session-list/', ChatSessionList.as_view()),
    path('chat-session-list/<uri>/', ChatSessionListDetail.as_view()),
    path('chat-session-create/', ChatSessionCreate.as_view()),
    path('chat-session-message-create/', ChatSessionMessageCreate.as_view()),
    path('chat-session-message-list/', ChatSessionMessageList.as_view()),
]