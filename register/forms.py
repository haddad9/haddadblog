from dataclasses import field
from multiprocessing import AuthenticationError
from django import forms
from django.contrib.auth import  login, authenticate
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User

class RegistrationForms(UserCreationForm):
   
    firstname = forms.CharField()
    lastname = forms.CharField()
    
    
    class Meta:
        model = User
        fields = ['firstname', 'lastname' , 'username','password1','password2']
        