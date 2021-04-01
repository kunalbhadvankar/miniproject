

from django.contrib.auth import authenticate, login as auth_login, logout as django_logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms  import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.contrib import messages
from django.urls import reverse
# Create your views here.


def main(request): 
    return render(request, "owner/layout.html")

def add_member(request):
    return render(request, "owner/add_member.html")

def pay_history(request):
    return render(request, "owner/history.html")

def menu(request):
    return render(request, "owner/menu.html")


def home(request):
    pass


def login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('main')
        else:
            return render(request, "owner/login.html", {
                "message": "invalid credentials"})
    return render(request, "owner/login.html")

def logout(request):
    django_logout(request)
    return render(request, 'owner/login.html')



