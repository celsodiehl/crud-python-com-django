from django.urls import path
from . import views

# Rotas Para usuário entrar e acessar a view
urlpatterns = [ #Quando u usuário acessar a localhost ele redireciona p/ view inicio
    path('', views.inicio, name='inicio')
]