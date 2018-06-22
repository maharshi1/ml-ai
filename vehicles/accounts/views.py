from accounts.forms import (
    UserRegistration,
    UserLogin
)
from django.contrib.auth import authenticate, login
from django.views.generic import (
    CreateView,
    FormView
)
from django.shortcuts import redirect
from django.utils.http import is_safe_url
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class RegisterView(CreateView):
    form_class = UserRegistration
    template_name = 'register.html'
    success_url = '/accounts/login'

    def dispatch(self, *args, **kwargs):
        if args[0].user.is_authenticated:
            return redirect('/home')
        return super().dispatch(*args, **kwargs)


class LoginView(FormView):
    form_class = UserLogin
    template_name = 'login.html'
    success_url = '/home'

    def dispatch(self, *args, **kwargs):
        if args[0].user.is_authenticated:
            return redirect('/home')
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        redirect_path = self.request.GET.get('next') \
            or self.request.POST.get('next') or None
        username = form.cleaned_data.get('phone_number')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            if is_safe_url(redirect_path, self.request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect('/home')
        return super(LoginView, self).form_invalid(form)


@login_required(login_url='accounts/login/')
def logout_user(request):
    logout(request)
    return redirect('/accounts/login/')
