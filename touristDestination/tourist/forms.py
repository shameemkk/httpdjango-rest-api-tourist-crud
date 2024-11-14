
from django import forms
from .models import Destination

class destinationForm(forms.ModelForm):
    image=forms.ImageField(required=False)
    class Meta:
        model=Destination
        fields='__all__'