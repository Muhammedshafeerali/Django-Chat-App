from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.login_user,name='login'),
    path('home/',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('room/<int:room_id>/', views.chat_room,name='chat_room'),
]
