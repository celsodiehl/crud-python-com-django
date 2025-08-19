from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#Função
def inicio(request):
    return HttpResponse("<h1>Bem Vindo a Biblioteca</h1>")