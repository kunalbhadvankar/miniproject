from django.urls import path
from . import views as views


urlpatterns = [
    
    path("", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("main/", views.main, name="main"),
    path("add_member/", views.add_member, name="add_member"),
    path("pay_history/", views.pay_history, name="pay_history"),
    path("menu/", views.menu, name="menu"),
    path("menu2/", views.menu2, name="menu2"),
    path("home/", views.home, name="home"),
    
    path("index/", views.index, name="index")
    
    
    
]
