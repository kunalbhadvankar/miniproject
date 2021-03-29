from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    return render(request, "owner/index.html")

def menu(request,Menu_id):
    menu=Menu.objects.all()
    context = {"menu": menu}
    return render(request, "owner/index.html",context)
   


def user(request):
    user = User.objects.all()
    return render(request, "owner/index.html")
