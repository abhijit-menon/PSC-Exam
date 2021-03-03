from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate
from .forms import RegistrationForm

# Create your views here.
def index(request):
    form = RegistrationForm()
    context = { "title":  "PSC-Exam",
                "form": form,
                 }
    return render(request, 'home/index.html', context)

def home(request):    
    return render(request, 'home/loggedin.html')

def faqs(request):
    return render(request, 'home/faq.html')

def user_home(request):
    context = { "user":  "Abhijit V",                
                 }
    return render(request,'home/user_home.html', context)