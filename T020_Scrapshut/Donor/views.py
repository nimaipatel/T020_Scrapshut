
from django.shortcuts import render, get_object_or_404
from core.models import Post, Requirement
from django.views import View

class Posts_page(View):

    def post_list(self, request):
        posts = Post.objects.all()
        requirements = Requirement.objects.all()
        return render(request,
                        'T020_Scrapshut/templates/test.html',
                        {'posts': posts, 'requirements': requirements})
        