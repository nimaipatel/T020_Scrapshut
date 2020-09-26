from django.db import models
from django.contrib.auth.models import User


class DonorClass(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    pincode = models.DecimalField(max_digits = 7, decimal_places = 0)
    phone_no = models.DecimalField(max_digits = 10, decimal_places = 0)
    
    def __srt__(self):
        return self.user.name