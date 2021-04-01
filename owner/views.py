

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms  import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.contrib import messages
from django.urls import reverse
# Create your views here.
def login(request):
    if request.method == 'POST':
        username =  request.POST.get('username')
        password = request.POST.get('password') 
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            messages.info(request, 'username or password is incorrect')
                  
    return render(request, "owner/login.html")

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
def logout(request):
    pass

