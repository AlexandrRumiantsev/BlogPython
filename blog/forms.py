import time
from django.forms import ModelForm
from blog.models import Post
from django import forms


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['author', 'title', 'text']
