from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import NgoAdmin


class NGOForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'password', 'email')


class NGOInfoForm(ModelForm):
    class Meta():
        model = NgoAdmin
        fields = ('address', 'pincode')
