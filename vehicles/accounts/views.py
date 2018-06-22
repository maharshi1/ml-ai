from django.shortcuts import render
from accounts.models import User
from accounts.forms import UserRegistration

def login(request):
    context = {

    }
    return render('login.html', context)

def register(request):
    register_form = UserRegistration(request.POST or None)
    context = {
        'register_form': register_form
    }
    if register_form.is_valid():
        register_form.save()
        return render(request, 'login.html', context)
    return render(request, 'register.html', context)
