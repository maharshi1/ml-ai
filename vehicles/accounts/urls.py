from django.urls import path
from accounts.views import (
    RegisterView,
    LoginView,
    logout_user
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='Register'),
    path('login/', LoginView.as_view(), name='Login'),
    path('logout/', logout_user, name='Logout')
]
