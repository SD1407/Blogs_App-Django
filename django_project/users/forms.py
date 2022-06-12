# here we are creating forms that we will modify and also we will inherit that UserCreationForm and we will add stuff
from django import forms  # importing forms
from django.contrib.auth.models import User  # importing User
from django.contrib.auth.forms import UserCreationForm # importing django default form  

class UserRegisterForm(UserCreationForm):  # created a class inherits that from UserCreationForm
    email = forms.EmailField()  # adds email field

    # check about this meta class also
    class Meta: # this meta class basically says that when we'll save the form the user will get saved at model table
        model = User
        fields = ['username', 'email', 'password1', 'password2']  # and fields would be in this same order