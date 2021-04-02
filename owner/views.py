

from django.contrib.auth import authenticate, login,logout 
from django.shortcuts import render, redirect
from django.contrib.auth.forms  import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
# Create your views here.

@login_required(login_url='login')
@admin_only
def main(request): 
    return render(request, "owner/layout.html")

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def add_member(request):
    return render(request, "owner/add_member.html")

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def pay_history(request):
    return render(request, "owner/history.html")

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def menu(request):
    menu = Menu.objects.all()
    return render(request, "owner/menu.html",{'menu': menu})

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def home(request):
    pass

@unauthenticated_user
def login_owner(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            return render(request, "owner/login.html", {
                "message": "invalid credentials"})
    return render(request, "owner/login.html")

def logout_owner(request):
    logout(request)
    return render(request, 'owner/login.html')



