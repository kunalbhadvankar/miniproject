from django.urls import path
from . import views as views

urlpatterns = [
    path("", views.index, name="index"),
]
