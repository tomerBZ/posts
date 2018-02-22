from django import forms
from django.core.validators import RegexValidator

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

    # alphanumeric = RegexValidator(r'^[a-zA-Z\s !\'-]*$', 'Only alphanumeric characters are allowed.')
    alphanumeric = RegexValidator(regex='^[a-zA-Z0-9 ]*$', message='Only alphanumeric characters are allowed.')
    post = forms.CharField(required=True)
    title = forms.CharField(required=True, validators=[alphanumeric])
    category = forms.CharField(required=True, validators=[alphanumeric])
    author = forms.CharField(required=True, validators=[alphanumeric])
