from . import views
from django.urls import path,include, re_path
from django.contrib.auth import views as auth_views

app_name = 'home'
SOCIAL_AUTH_URL_NAMESPACE = "home:social"

urlpatterns = [
    path('', views.index, name='index'),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('home/',views.home, name="home"),
    path("logout/",auth_views.LogoutView.as_view(), name="logout"),
    path("faqs/",views.faqs, name="faqs")
    
]