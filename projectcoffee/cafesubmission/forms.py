from django import forms
from .models import CafeSubmission

class CafeSubmissionForm(forms.ModelForm):

    class Meta:
        model = CafeSubmission
        fields = ('name', 'description', 'email', 'address', 'website' , 'hours', 'phone', 'image',)

    

