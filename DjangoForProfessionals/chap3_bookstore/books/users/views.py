from django.shortcuts import render

from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomerCreationForm

# Create your views here.

class SignupPageView(generic.CreateView):
    form_class = CustomerCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
