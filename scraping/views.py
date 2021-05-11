from django.shortcuts import render

# Create your views here.
from django.views import generic
from scraping.models import News



class HomePageView(generic.ListView):
    template_name = 'home.html'

    def get_queryset(self):
    	return News.objects.all()