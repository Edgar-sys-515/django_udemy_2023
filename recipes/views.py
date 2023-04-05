from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):

    return render(request, 'recipes/home.html', context={'nome': 'Edgar'})


def sobre(request):

    return HttpResponse("Sobre Novo")


def contato(request):

    return HttpResponse("Contato Novo")
