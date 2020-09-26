from django.shortcuts import render
from .models import NgoAdmin, Post, Requirement


def index(request):
    return render(request, template_name='../templates/test.html')
