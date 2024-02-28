from django.urls import path
from . import views


urlpatterns = [
    path('', views.chat_view, name='chat'),
    path('clear-chat/', views.clear_chat, name='clear_chat'),
]