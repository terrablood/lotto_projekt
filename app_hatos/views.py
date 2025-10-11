from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.

def kerdesek(request: HttpRequest):
    template = 'app_hatos/index.html'
    context = {}
    return render(request, template, context)

  

def elso(request: HttpRequest):
    template = 'app_hatos/elso.html'
    context = {}
    return render(request, template, context)
def masodik(request: HttpRequest):
    template = 'app_hatos/masodik.html'
    context = {}
    return render(request, template, context)
def harmadik(request: HttpRequest):
    template = 'app_hatos/harmadik.html'
    context = {}
    return render(request, template, context)
def negyedik(request: HttpRequest):
    template = 'app_hatos/negyedik.html'
    context = {}
    return render(request, template, context)
def otodik(request: HttpRequest):
    template = 'app_hatos/otodik.html'
    context = {}
    return render(request, template, context)