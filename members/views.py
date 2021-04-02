from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.contrib import messages
from django.urls import reverse

# Create your views here.


def main(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse("login"))
    return render(request,"members/main.html")


