from django.shortcuts import render,redirect

from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

@login_required(login_url='/')
def home(request):

    return render(request,'index.html')

@login_required(login_url='/')
def chat_room(request,room_id):

    return render(request, 'chat_room.html', {'room_id': room_id})



def login_user(request):
    if request.method=='POST':
        name=request.POST['name']
        password=request.POST['password']
        user = authenticate(request,username=name, password=password)
        if user:
            login(request,user)
            return redirect(home)

        else:
            pass

    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        name=request.POST['name']
        password=request.POST['password']
        if User.objects.filter(username=name).exists():
            messages.info(request,'username is already taken')
            return render(request,'register.html')
        else:
            user=User.objects.create_user(username=name,password=password) 
            return redirect(home)   
    return render(request,'register.html')