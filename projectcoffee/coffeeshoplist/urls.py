from django.urls import path
from . import views
from django.urls import include
from .views import register, login
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.coffeeshoplist, name='coffeeshoplist'),
    path('register/', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', views.login, name='login'),
    path('accounts/logout/',  auth_views.LogoutView.as_view(), name='logout'),
    path('rate_shop/<int:coffee_shop_id>/', views.rate_coffee_shop, name='rate_shop'),
    path('shop_reviews/<int:coffee_shop_id>/', views.shopreviews, name='shop_reviews'),
]