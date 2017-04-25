from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ['name', 'email', 'url', 'text']

    widgets = {
      'name': forms.TextInput(attrs = {'placeholder': 'Username'}),
      'email': forms.TextInput(attrs = {'placeholder': 'Email'}),
      'url': forms.TextInput(attrs = {'placeholder': 'Website'})
    }