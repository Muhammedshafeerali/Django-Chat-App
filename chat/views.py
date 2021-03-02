from django.shortcuts import render

# Create your views here.


def home(request):

    return render(request,'index.html')

def chat_room(request,room_id):
    
    return render(request, 'chat_room.html', {'room_id': room_id})
