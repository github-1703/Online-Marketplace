from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username= forms.CharField(widget=forms.TextInput(attrs=({
        'placeholder':'Username',
        'class':'w-full rounded-md border-0 py-1.5 px-6 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6',
    })))
    
    password=forms.CharField(widget=forms.PasswordInput(attrs=({
        'placeholder':'Your Password',
        'class':'w-full rounded-md border-0 py-1.5 px-6 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6',
    })))

class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username','email','password1','password2')
    
     
    username=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Username',
        'class':'w-full rounded-md border-0 py-1.5 px-6 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6',
    }))
    
    email=forms.CharField(widget=forms.EmailInput(attrs=({
        'placeholder':'Email',
        'class':'w-full rounded-md border-0 py-1.5 px-6 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6',    
    })))
    
    password1=forms.CharField(widget=forms.PasswordInput(attrs=({
        'placeholder':'Password',
        'class':'w-full rounded-md border-0 py-1.5 px-6 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6',    
    })))
    
    password2=forms.CharField(widget=forms.PasswordInput(attrs=({
        'placeholder':'Confirm Password',
        'class':'w-full rounded-md border-0 py-1.5 px-6 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6',
    })))