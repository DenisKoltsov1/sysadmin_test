from django.shortcuts import render

from django.views.generic import CreateView
from .models import MyUser
from django.contrib.auth.views import LoginView as LoginViewContrib , LogoutView as LogoutViewContrib
from .forms import RegisterForm


class RegisterView(CreateView):
    model = MyUser
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = '/login/'


class LoginView(LoginViewContrib):
    template_name = 'login.html'

    # self.request.user


class LogoutView(LogoutViewContrib):
    pass