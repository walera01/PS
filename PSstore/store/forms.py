from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import *


class TestForm(forms.ModelForm):
    class Meta:
        model = TestModel
        exclude = ['']


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')
        widgets = {
            'email' : forms.EmailInput(attrs = {'class':'form-input'}),
            'username': forms.TextInput(attrs = {'class':'form-input'}),
            'password1': forms.PasswordInput(attrs = {'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs = {'class': 'form-input'})

        }

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs = {'class':'form-input'}))
    password = forms.CharField(label = "Password", widget=forms.PasswordInput(attrs = {'class':'form-input'}))