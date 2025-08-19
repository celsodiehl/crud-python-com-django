from django.urls import path
from . import views

# Rotas Para usuário entrar e acessar a view
urlpatterns = [ #Quando u usuário acessar a localhost ele redireciona p/ view inicio
    path('', views.inicio, name='inicio'),
    path('outros', views.outros, name='outros'), #Chamada de seção/página outros
    path('livros', views.livros, name='livros'), #Rota para livros
]