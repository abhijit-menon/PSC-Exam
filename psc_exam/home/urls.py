from . import views
from django.urls import path,include
from django.contrib.auth import views as auth_views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),   
    path('home/',views.home, name="home"),
    path("logout/",auth_views.LogoutView.as_view(), name="logout"),
    path("faqs/",views.faqs, name="faqs"),
    path("user-home/",views.user_home, name="user_home")
    
]