# forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class FormLogin(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(attrs={'class':'form-control', 'type':'text'}),
    )
     
    password = forms.CharField(
        widget= forms.PasswordInput(attrs={'class':'form-control'}),
    )







