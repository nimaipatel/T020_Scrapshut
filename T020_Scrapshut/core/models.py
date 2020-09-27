from django.db import models
from django.contrib.auth.models import User


class NgoAdmin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    pincode = models.IntegerField(default=0)

    def __srt__(self):
        return self.user.name


class Post(models.Model):
    NgoAdmin = models.ForeignKey(NgoAdmin, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    quantity = models.IntegerField(default=1)
    completed = models.IntegerField(default=0)

    def __str__(self):
        return '{}: {}'.format(self.title, self.description)


class Requirement(models.Model):
    Post = models.ForeignKey(Post, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    completed = models.IntegerField(default=0)
    requirement_name = models.CharField(max_length=50)

    def __str__(self):
        return '{} ({})'.format(self.requirement_name, self.quantity)
