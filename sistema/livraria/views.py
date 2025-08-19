from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#Função inicio
def inicio(request):
    return HttpResponse("<h1>Bem Vindo a Biblioteca</h1>")
#Função outros
def outros(request):
    return render(request, 'paginas/outros.html')
#Função livros
def livros(request):
    return render(request, 'livros/index.html')