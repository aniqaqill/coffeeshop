from django import forms
from .models import Rating
from django_star_ratings.widgets import StarRatingInput


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating', 'review']
        widgets = {
            'rating': StarRatingInput(),
        }
