from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.\
class CoffeeShop(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    hours = models.CharField(max_length=100)
    image = models.ImageField(upload_to='coffee_shop_images/', default='coffee_shop_images/default.jpg')
class Rating(models.Model):
    coffee_shop = models.ForeignKey(CoffeeShop, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.TextField(blank=True)
