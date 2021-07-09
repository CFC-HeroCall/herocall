from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#Form to add a new user to the database. Adds a username, an email and a password
#The second password is to make sure the user typed the right one 
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']