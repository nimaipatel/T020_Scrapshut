from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import DonorClass


class DonorForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')

class DonorInfoForm(ModelForm):
     class Meta():
         model = DonorClass
         fields = ('address','pincode')

