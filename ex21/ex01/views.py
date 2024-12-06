from django.shortcuts import render
from .models import PesquisaOpiniao, Escolhas

def lista_pesquisas(request):
    pesquisas = PesquisaOpiniao.objects.all()
    return render(request, 'lista_pesquisas.html', {'pesquisas': pesquisas})