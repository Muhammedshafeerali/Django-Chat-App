from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('room/<int:room_id>/', views.chat_room,name='chat_room'),
]
