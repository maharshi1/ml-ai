from motor.forms import MotorForm
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class HomeView(CreateView):
    form_class = MotorForm
    template_name = 'home.html'
    success_url = '/home'
