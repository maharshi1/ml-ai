from django.shortcuts import render
from accounts.models import User
from accounts.forms import (
    UserRegistration,
    UserLogin
)
from django.contrib.auth import authenticate

def login(request):
    login_form = UserLogin(request.POST or None)
    context = {
        'login_form': login_form
    }
    if login_form.is_valid():
        phone_number = login_form.cleaned_data.get('phone_number')
        password = login_form.cleaned_data.get('password')
        FIX LOGIN
        user = authenticate(phone_number, password)
    return render(request, 'login.html', context)

def register(request):
    register_form = UserRegistration(request.POST or None)
    context = {
        'register_form': register_form
    }
    if register_form.is_valid():
        register_form.save()
        return render(request, 'login.html', context)
    return render(request, 'register.html', context)
