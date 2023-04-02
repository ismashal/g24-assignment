from django import forms
from .models import City_Info


class City_Info_form(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = City_Info
 
        # specify fields to be used
        fields = [
            "City",
            "Population",
        ]