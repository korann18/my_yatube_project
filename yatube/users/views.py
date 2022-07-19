from django.shortcuts import render

from django.views.generic import CreateView

from django.urls import reverse_lazy

from .forms import CreationForm
from django.conf import settings


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy(settings.LOGOUT_REDIRECT_URL)
    template_name = 'users/signup.html'
