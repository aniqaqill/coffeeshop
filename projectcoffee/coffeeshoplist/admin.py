from django.contrib import admin

# Register your models here.
from .models import CoffeeShop, Rating

admin.site.register(CoffeeShop)
admin.site.register(Rating)
