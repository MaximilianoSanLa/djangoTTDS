from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
class homeView(TemplateView):
    template_name='aviones/home.html'