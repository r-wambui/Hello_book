# -*- coding: utf-8 -*-

from django.shortcuts import render
from forms import UserRegisterForm, UserLoginForm
from django.http import HttpResponseRedirect
from django import forms

from models import User


def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            role = form.cleaned_data['role']
            if not User.objects.filter(email=email).exists():
                p = User(email=email, password=password, role=role)
                print(p.email)
                p.save()
                return HttpResponseRedirect('/login/')
            else:
                raise forms.ValidationError('User with the email exist')
    else:
        form = UserRegisterForm()

    return render(request, 'register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        pass
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})
