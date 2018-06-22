from django.shortcuts import render
from django.http import HttpResponse
from motor.models import Motor
from motor.forms import MotorForm

def home(request):
    motor = MotorForm(request.POST or None)
    context = {
        'motor': motor
    }
    return render(request, 'home.html', context)
