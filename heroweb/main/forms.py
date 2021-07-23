from django import forms
from main.models import Post

class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']