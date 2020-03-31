from django.shortcuts import render

from django.views.generic import Listview

from .models import Post

# Create your views here.

class HomePageView(Listview):
    model = Post
    template_name =  'home.html'
