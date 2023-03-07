from django.shortcuts import render, redirect
from .models import CoffeeShop, Rating
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import RatingForm
from .forms import UserRegistrationForm

def coffeeshoplist(request):
    coffee_shops = CoffeeShop.objects.all()
    ratings = Rating.objects.all()
    rating_dict = {}
    for rating in ratings:
        rating_dict.setdefault(rating.coffee_shop_id, []).append(rating.rating)
    avg_ratings = {}
    for coffee_shop in coffee_shops:
        ratings_list = rating_dict.get(coffee_shop.id, [])
        avg_rating = round(sum(ratings_list) / max(len(ratings_list), 1), 2) if ratings_list else '-'
        avg_ratings[coffee_shop.id] = avg_rating
    return render(request, 'coffeeshoplist.html', {'coffee_shops': coffee_shops, 'avg_ratings': avg_ratings})


# view for all the reviews of a coffee shop
def shopreviews(request, coffee_shop_id):
    coffee_shop = CoffeeShop.objects.get(id=coffee_shop_id)
    ratings = Rating.objects.filter(coffee_shop=coffee_shop)
    return render(request, 'shop_reviews.html', {'coffee_shop': coffee_shop, 'ratings': ratings})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
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
 
 
        
    





