from django.urls import path
from . import views as views

urlpatterns = [
    path("", views.index, name="index"),
     path("add_member/", views.add_member, name="add_member"),
    path("pay_history/", views.pay_history, name="pay_history"),
    path("menu", views.menu, name="menu")
    
    
    
]
