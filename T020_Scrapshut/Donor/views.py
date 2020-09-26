
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from core.models import Post, Requirement
from django.views import View
from .forms import DonorForm, DonorInfoForm

def post_list(request):
    posts = Post.objects.all()
    requirements = Requirement.objects.all()
    username = DonorForm.objects.username
    return render(request,'../templates/test.html',{'posts': posts, 'requirements': requirements, 'username': username})

def donor_reg(request):
    registered =  False
    if request.method == 'POST' :
        user_form = DonorForm(request.POST)
        info_form = DonorInfoForm(request.POST)
        if user_form.is_valid() and info_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            info = info_form.save(commit=False)
            info.user = user
            info.save()
            registered = True
        else:
            print(user_form.errors,info_form.errors)
    else:
        user_form = DonorForm()
        info_form = DonorInfoForm()
    return render(request,'../templates/register.html',
                          {'user_form':user_form,
                           'info_form':info_form,
                           'registered':registered})

def donor_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('Donor:homepage')
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, '../templates/login.html', {})
        

        