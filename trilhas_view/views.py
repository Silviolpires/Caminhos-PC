from django.shortcuts import render, get_object_or_404
from .models import Trilha

def lista_trilhas(request):
    trilhas = Trilha.objects.all()
    return render(request, 'trilhas_view/lista_trilhas.html', {'trilhas': trilhas})

def detalhe_trilha(request, trilha_id):
    trilha = get_object_or_404(Trilha, pk=trilha_id)
    return render(request, 'trilhas_view/detalhe_trilha.html', {'trilha': trilha})