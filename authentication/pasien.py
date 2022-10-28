#OK

from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView

from .forms import PasienSignUpForm
from .models import User

class PasienSignUpView(CreateView):
    model = User
    form_class = PasienSignUpForm
    template_name = 'register_pasien.html'  ## ?

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Pasien'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('authentication:login')