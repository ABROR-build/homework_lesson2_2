from django.db import models
from django.contrib.auth.models import AbstractUser


class ClientsAndSellers(AbstractUser):
    age = models.IntegerField(default=20)
    is_seller = models.FloatField(default=False)
    tel_number = models.CharField(max_length=200)
