from django import forms
from django.forms import fields, widgets

from .models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ["user"]
        widgets = {
            'title': widgets.TextInput(attrs={
                'placeholder': 'Title',
                'class': 'form-control cc-exp'
            }),
            'caption': widgets.TextInput(attrs={
                'placeholder': 'Caption',
                'class': 'form-control cc-exp'
            }),
            'thumbnail_image': widgets.FileInput(attrs={
                'placeholder': 'Thumbnail Image',
                'class': 'form-control cc-exp'
            }),
            'content': widgets.Textarea(attrs={
                'placeholder': 'Content',
                'class': 'form-control cc-exp'
            }),
        }
