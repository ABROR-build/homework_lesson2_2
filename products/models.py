from django.db import models
from django.contrib.auth import get_user_model


class Products(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    product_name = models.CharField(max_length=400)
    expiry_date = models.DateField()
    price = models.FloatField()

    def __str__(self):
        return self.product_name
