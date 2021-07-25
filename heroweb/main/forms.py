from django import forms
from main.models import Post

class PostCreationForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Post
        fields = ['title', 'text']