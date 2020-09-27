from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import NgoAdmin, Post, Requirement


class NGOForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'password', 'email')


class NGOInfoForm(ModelForm):
    class Meta():
        model = NgoAdmin
        fields = ('address', 'pincode')

class PostForm(ModelForm):
    class Meta():
        model = Post
        fields = ('title', 'description')

class RequirementForm(ModelForm):
    class Meta():
        model = Requirement
        fields = ('requirement_name', 'quantity')
