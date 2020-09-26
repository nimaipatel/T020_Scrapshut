
from django.shortcuts import render, get_object_or_404
from core.models import Post, Requirement
from django.views import View


def post_list(request):
    posts = Post.objects.all()
    requirements = Requirement.objects.all()
    return render(request,'../templates/test.html',{'posts': posts, 'requirements': requirements})
        