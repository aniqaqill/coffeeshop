from django.urls import path
from . import views
from django.urls import include
from .views import register, login

urlpatterns = [
    path('', views.coffeeshoplist, name='coffeeshoplist'),
    path('register/', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', views.login, name='login'),
]