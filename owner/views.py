from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def main(request):
    return render(request, "owner/layout.html")

def add_member(request):
    return render(request, "owner/add_member.html")

def pay_history(request):
    return render(request, "owner/history.html")

def menu(request):
    return render(request, "owner/menu.html")

