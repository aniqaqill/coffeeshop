from django.shortcuts import render, redirect
from .models import CoffeeShop
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import RatingForm

def coffeeshoplist(request):
    coffee_shops = CoffeeShop.objects.all()
    if request.user.is_authenticated:
        # If the user is authenticated, show them the coffee shop list along with a welcome message
        context = {'coffee_shops': coffee_shops}
    else:
        # If the user is not authenticated, only show them the coffee shop list
        context = {'coffee_shops': coffee_shops}
    return render(request, 'coffeeshoplist.html', context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render({}, request))

@login_required
def rate_coffee_shop(request, coffee_shop_id):
    coffee_shop = CoffeeShop.objects.get(id=coffee_shop_id)
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.coffee_shop = coffee_shop
            rating.user = request.user
            rating.save()
            return redirect('coffeeshoplist')
    else:
        form = RatingForm()
    return render(request, 'rate_shop.html', {'form': form, 'coffee_shop': coffee_shop})
 
 
        
    





