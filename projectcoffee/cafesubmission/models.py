
# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class CafeSubmission(models.Model):
  name = models.CharField(max_length=100)
  address = models.CharField(max_length=255)
  phone = models.CharField(max_length=100)    
  website = models.CharField(max_length=100)
  email = models.CharField(max_length=100)
  description = models.CharField(max_length=100)
  hours = models.CharField(max_length=100)
  image = models.ImageField(upload_to='coffee_shop_images/', default='coffee_shop_images/default.jpg')
  submitted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cafe_submissions')

  def __str__(self):
        return self.name