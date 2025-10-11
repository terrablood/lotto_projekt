from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.

def kerdesek(request: HttpRequest):
    template = 'app_hatos/index.html'
    context = {}
    return render(request, template, context)

# 1 
#Készítsen lekérdezést, amely megadja, hogy az előző évezredben (2001. január 1. előtt)
#mikor volt hat találatos szelvény! A húzáshoz tartozó évet és hetet jelenítse meg időrendben!
def elso(request: HttpRequest):
    template = 'app_hatos/elso.html'
    
    huzasok = Huzas.objects.all
    nyermenyek = Nyeremeny.objects.all
    hatos_talalatok = []

    for nyeremeny in nyermenyek:
        if(nyeremeny.talalat == 6):
            for huzas in huzasok:
                if(huzas.ev >= 2001, huzas.idd == nyeremeny.huzasid):
                    hatos_talalatok.append(huzas.ev)

    context = {
        'hatosok_2001elott' : hatos_talalatok,
    }
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