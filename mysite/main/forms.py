from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]

class LoginForm(forms.Form):
    uname = forms.CharField(max_length=100, required=True)
    pword = forms.CharField(max_length=100, required=True)