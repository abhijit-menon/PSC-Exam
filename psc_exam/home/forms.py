from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    full_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Full Name'}))
    email = forms.EmailField(max_length=75, widget=forms.TextInput(attrs={'placeholder': 'Your email will be used to reset password'}))
    phone = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'placeholder': 'Enter your 10 digit mobile number only'}))

    class Meta:
        model = User
        fields = ("full_name","email","phone","password1","password2")

 