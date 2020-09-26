from django.db import models
from django.contrib.auth.models import User


class DonorClass(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    pincode = models.IntegerField()

    def __srt__(self):
        return self.user.name

