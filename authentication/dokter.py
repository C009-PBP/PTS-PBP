#OK

from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView

from .forms import DokterSignUpForm
from .models import User


class DokterSignUpView(CreateView):
    model = User
    form_class = DokterSignUpForm
    template_name = 'register_dokter.html'  ## ?

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Dokter'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('authentication:login')