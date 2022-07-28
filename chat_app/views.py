from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from django.core.serializers import serialize
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

import json
# Create your views here.

@login_required
def Home(request):
    if request.method == "POST":
        room_name = request.POST.get("room_name", None)
        if room_name is None:
            return HttpResponse(status=400)
        if models.ChatRoom.objects.filter(name=room_name).exists():
            return HttpResponse(status=405)
        else:
            models.ChatRoom.objects.create(name=room_name)
            rooms = models.ChatRoom.objects.all()
            return render(request, "base.html", {'qs': rooms})
    else:
        rooms = models.ChatRoom.objects.all()
        return render(request, "base.html", {'qs': rooms})



def Register(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('/login/')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'registration.html', context)


def Login(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.error(request, "Username or password is wrong")
            return redirect("/login/")
    return render(request, "login.html")


def Logout(request):
    logout(request)
    messages.info(request, "You are logged out now")
    return redirect("/login/")