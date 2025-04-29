from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Trilha
from .forms import TrilhaForm

def lista_trilhas(request):
    trilhas = Trilha.objects.all()
    return render(request, 'trilhas_view/lista_trilhas.html', {'trilhas': trilhas})

def detalhe_trilha(request, trilha_id):
    trilha = get_object_or_404(Trilha, pk=trilha_id)
    return render(request, 'trilhas_view/detalhe_trilha.html', {'trilha': trilha})

def criar_trilha(request):
    if request.method == 'POST':
        form = TrilhaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Trilha criada com sucesso!')
            return redirect('trilhas_view:lista_trilhas')
    else:
        form = TrilhaForm()
    
    return render(request, 'trilhas_view/form_trilha.html', {
        'form': form,
        'titulo': 'Nova Trilha',
        'botao': 'Criar'
    })

def editar_trilha(request, trilha_id):
    trilha = get_object_or_404(Trilha, pk=trilha_id)
    
    if request.method == 'POST':
        form = TrilhaForm(request.POST, instance=trilha)
        if form.is_valid():
            form.save()
            messages.success(request, 'Trilha atualizada com sucesso!')
            return redirect('trilhas_view:detalhe_trilha', trilha_id=trilha.id)
    else:
        form = TrilhaForm(instance=trilha)
    
    return render(request, 'trilhas_view/form_trilha.html', {
        'form': form,
        'titulo': f'Editar Trilha: {trilha.nome}',
        'botao': 'Atualizar'
    })

def excluir_trilha(request, trilha_id):
    trilha = get_object_or_404(Trilha, pk=trilha_id)
    
    if request.method == 'POST':
        trilha.delete()
        messages.success(request, 'Trilha excluída com sucesso!')
        return redirect('trilhas_view:lista_trilhas')
    
    return render(request, 'trilhas_view/confirmar_exclusao.html', {'trilha': trilha})