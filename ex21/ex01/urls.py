from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_pesquisas, name='lista_pesquisas'),
]