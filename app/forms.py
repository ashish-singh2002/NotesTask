from django import forms
from .models import Ashish

class AshishForm(forms.ModelForm):
    class Meta:
        model = Ashish
        fields = ['title', 'content', 'timestamp']
       
