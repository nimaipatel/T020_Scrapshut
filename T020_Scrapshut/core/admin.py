from django.contrib import admin
from .models import NgoAdmin, Post, Requirement

admin.site.register(NgoAdmin)
admin.site.register(Post)
admin.site.register(Requirement)
