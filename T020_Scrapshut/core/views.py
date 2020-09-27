from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .models import NgoAdmin, Post, Requirement
from .forms import NGOForm, NGOInfoForm


def index(request):
    return render(request, template_name='../templates/test.html')


def register(request):
    registered = False
    if request.method == 'POST':
        NGO_Form = NGOForm(request.POST)
        NGO_Info_Form = NGOInfoForm(request.POST)
        if NGO_Form.is_valid() and NGO_Info_Form.is_valid():
            NGO = NGO_Form.save()
            NGO.set_password(NGO.password)
            NGO.save()
            info = NGO_Info_Form.save(commit=False)
            info = NGO_Info_Form.save(commit=False)
            info.user = NGO
            info.save()
            registered = True
        else:
            print(NGO_Form.errors, NGO_Info_Form.errors)
    else:
        NGO_Form = NGOForm()
        NGO_Info_Form = NGOInfoForm()
    return render(request, '../templates/signupngo.html', {
        'NGO_Form': NGO_Form,
        'NGO_Info_Form': NGO_Info_Form
    })


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('Donor:homepage')
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(
                username, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, '../templates/NGOlogin.html', {})


def PostCreate(request):
    if request.method == 'POST':
        Post_content = Post(request.POST)
        requirement = Requirement(request.POST)
        if Post_content.is_valid() and requirement.is_valid():
            Post_content.save()
            requirement.save()
            return redirect('Donor:homepage')
    else:
        Post_content = Post()
        requirement = Requirement()
    return(request, '../templates/post_create.html', {'Post_content': Post_content,
                                                      'requirement': requirement})
