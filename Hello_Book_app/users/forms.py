from django.forms import ModelForm
from django import forms
from models import User
# from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = '__all__'


class UserLoginForm(ModelForm):

    class Meta:
        model = User
        exclude = ['role']
