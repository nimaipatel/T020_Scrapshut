from django.contrib import admin
from django.urls import path, include
from .views import post_list

urlpatterns = [
path('', post_list)
]