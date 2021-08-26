from django.forms import ModelForm, widgets
from .models import Bizhub


class BusinessCreationForm(ModelForm):
    class Meta:
        model = Bizhub
        fields = [
            "business_name",
            "business_sector",
            "description",
            "location",
            "contact",
            "website",
        ]

        widgets = {
            'business_name': widgets.TextInput(attrs={
                'placeholder': 'Business Name',
                'class': 'form-control cc-exp'
            }),
            'business_sector': widgets.Select(attrs={
                'placeholder': 'Bussiness Sector',
                'class': 'form-control cc-exp'
            }),
            'description': widgets.Textarea(attrs={
                'placeholder': 'Business Description',
                'class': 'form-control cc-exp',
                'style': 'max-height: 100px'
            }),
            'location': widgets.Textarea(attrs={
                'placeholder': 'Location',
                'class': 'form-control cc-exp',
                'style': 'max-height: 100px'
            }),
            'contact': widgets.TextInput(attrs={
                'placeholder': 'contact',
                'class': 'form-control cc-exp'
            }),
            'website': widgets.URLInput(attrs={
                'placeholder': 'https://www.example.com/',
                'class': 'form-control cc-exp'
                
            })
        }