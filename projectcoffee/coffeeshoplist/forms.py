from django import forms
from .models import Rating
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating', 'review']
 
class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

