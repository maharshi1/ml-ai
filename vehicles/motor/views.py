from motor.forms import MotorForm
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class HomeView(CreateView):
    form_class = MotorForm
    template_name = 'home.html'
    success_url = '/home'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(HomeView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super(HomeView, self).get_context_data(**kwargs)
        ctx['vehicles'] = self.form_class.Meta.model.objects.filter(
            user=self.request.user)
        return ctx
