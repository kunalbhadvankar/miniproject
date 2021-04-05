from django.contrib.auth import authenticate, login as auth_login, logout as django_logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms  import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm 
# Create your views here.

@unauthenticated_user
def login(request):
    if request.method == 'POST':
        username =  request.POST.get('username')
        password = request.POST.get('password') 
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('main')
        else:
            return render(request, "owner/login.html",{
                "message": "invalid credentials"
            })
                  
    return render(request, "owner/login.html")

@login_required(login_url='login')
@admin_only
def main(request):
    return render(request, "owner/main.html")

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def add_member(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, "owner/add_member.html", context)

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

def logout(request):
    django_logout(request)
    return render(request, 'owner/login.html')


def index(request):
    return render(request, 'owner/index.html')

def menu2(request):
    menu = Menu.objects.all()
    return render(request, "owner/menu2.html",{'menu': menu}) 




