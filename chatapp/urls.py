from django.urls import path
from . import views


urlpatterns = [
    path('', views.Signup, name='signup'),
    path('login/', views.Login, name='login'),
    path('chat/', views.ChatPage, name='chat'),
    path('logout/', views.LogoutPage, name='logout'),
]