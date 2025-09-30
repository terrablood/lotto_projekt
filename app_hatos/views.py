from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.

def kerdesek(request: HttpRequest):
    template = 'app_hatos/index.html'
    context = {}
    return render(request, template, context)