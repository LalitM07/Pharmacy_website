from django import forms
from django.contrib.auth import authenticate ,get_user_model,login,logout
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm




class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model  = User
        fields = ['username','first_name','last_name','email','password']