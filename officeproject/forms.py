from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):   #form for taking new internadmin details
    username = forms.CharField(label="Your Username")
    password1 = forms.CharField(label="Your Password",widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat Your Password",widget=forms.PasswordInput)
    email = forms.EmailField(label = "Email Address")
    first_name = forms.CharField(label = "Name")
    last_name = forms.CharField(label = "Surname")



    # this sets the order of the fields
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "username", "password1", "password2", )
