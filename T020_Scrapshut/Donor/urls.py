from django.contrib import admin
from django.urls import path, include
from .views import post_list, donor_reg, donor_login

app_name = 'Donor'

urlpatterns = [
path('', post_list, name = 'homepage'),
path('register/', donor_reg, name = 'register'),
path('login/', donor_login, name = 'login')
]