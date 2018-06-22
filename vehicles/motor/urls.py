from django.urls import path
from motor.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='Home'),
]
