from django.shortcuts import render
from .models import UserProfile
from .forms import SignupForm
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


# Create your views here.
class SignupView(CreateView):
    form_class = SignupForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('articles:home')


class ProfilePageView(LoginRequiredMixin, TemplateView):
    template_name = 'registration/profile-page.html'