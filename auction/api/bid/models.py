from django.contrib.auth.models import User
from django.db import models
from auction.api.product.models import Product
from user.models import User


class Bid(models.Model):
    id = models.BigAutoField(help_text="bid id", primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    success = models.BooleanField(default=False)
