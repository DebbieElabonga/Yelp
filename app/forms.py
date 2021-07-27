from django import forms
from .models import Post, Review
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('image','name', 'caption')
class ReviewForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['review'].widget = forms.TextInput()
        self.fields['review'].widget.attrs['placeholder'] = 'Add a review...'
    class Meta:
        model = Review
        fields = ('review',)