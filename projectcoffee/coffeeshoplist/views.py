from django.shortcuts import render, redirect
from .models import CoffeeShop
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm

def coffeeshoplist(request):
    coffee_shops = CoffeeShop.objects.all()
    # return HttpResponse("Test")
    template = loader.get_template('coffeeshoplist.html')
    return HttpResponse(template.render({'coffee_shops': coffee_shops}, request))

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

 
        
    





