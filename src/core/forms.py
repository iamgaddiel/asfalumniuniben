from django import forms
from django.contrib.auth.models import User
from django.db.models import fields
from django.forms import widgets
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': widgets.TextInput(attrs={'placeholder': 'Username'}),
            'email': widgets.TextInput(attrs={'placeholder': 'Email'}),
            'password1': widgets.PasswordInput(attrs={'placeholder': 'Password'}),
            'password2': widgets.PasswordInput(attrs={'placeholder': 'Confirm Password'}),
        }


class ProfileCreationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'full_name', 
            'title', 
            # 'profile_image', 
            'day_of_birth', 
            'month_of_birth',  
            'phone_number', 
            'country', 
            'state', 
            'profession', 
            'ministry_group', 
            'year_of_graduation'
        ]
        widgets = {
            'full_name': widgets.TextInput(attrs={
                'placeholder': 'Fullname',
                'class': 'form-control cc-exp'
            }),
            'title': widgets.Select(attrs={
                'placeholder': 'Fullname',
                'class': 'form-control cc-exp'
            }),
            'day_of_birth': widgets.Select(attrs={
                'placeholder': 'Fullname',
                'class': 'form-control cc-exp'
            }),
            'month_of_birth': widgets.Select(attrs={
                'placeholder': 'Fullname',
                'class': 'form-control cc-exp'
            }),
            'phone_number': widgets.TextInput(attrs={
                'placeholder': 'Phone Number',
                'class': 'form-control cc-exp'
            }),
            'country': widgets.TextInput(attrs={
                'placeholder': 'Country of Residence',
                'class': 'form-control cc-exp'
            }),
            'state': widgets.TextInput(attrs={
                'placeholder': 'State',
                'class': 'form-control cc-exp'
            }),
            'profession': widgets.TextInput(attrs={
                'placeholder': 'Profession',
                'class': 'form-control cc-exp'
            }),
            'ministry_group': widgets.TextInput(attrs={
                'placeholder': 'ASF Ministry Group',
                'class': 'form-control cc-exp'
                
            }),
            'year_of_graduation': widgets.TextInput(attrs={
                'placeholder': 'Year Of Graduation',
                'class': 'form-control cc-exp'
                
            })
        }
