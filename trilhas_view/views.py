from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from home_view.models import PessoaFisica
from .models import Trilha
from .forms import TrilhaForm
from .utils import admin_required  # Importar o decorador

def lista_trilhas(request):
    trilhas = Trilha.objects.all()
    # Adicionar verificação se o usuário é staff ou superuser
    is_admin = False
    if request.user.is_authenticated:
        is_admin = request.user.is_superuser or request.user.is_staff
    
    return render(request, 'trilhas_view/lista_trilhas.html', {
        'trilhas': trilhas,
        'is_admin': is_admin
    })

def detalhe_trilha(request, trilha_id):
    trilha = get_object_or_404(Trilha, pk=trilha_id)
    # Adicionar verificação se o usuário é staff ou superuser
    is_admin = False
    if request.user.is_authenticated:
        is_admin = request.user.is_superuser or request.user.is_staff
    
    return render(request, 'trilhas_view/detalhe_trilha.html', {
        'trilha': trilha,
        'is_admin': is_admin
    })

@admin_required
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

@admin_required
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

@admin_required
def excluir_trilha(request, trilha_id):
    trilha = get_object_or_404(Trilha, pk=trilha_id)
    
    if request.method == 'POST':
        trilha.delete()
        messages.success(request, 'Trilha excluída com sucesso!')
        return redirect('trilhas_view:lista_trilhas')
    
    return render(request, 'trilhas_view/confirmar_exclusao.html', {'trilha': trilha})

@admin_required
def gerenciar_guias(request, trilha_id):
    trilha = get_object_or_404(Trilha, pk=trilha_id)
    
    if request.method == 'POST':
        # Obter os IDs dos guias selecionados
        guias_ids = request.POST.getlist('guias')
        
        # Limpar os guias atuais
        trilha.guias.clear()
        
        # Adicionar os guias selecionados
        if guias_ids:
            guias = PessoaFisica.objects.filter(id__in=guias_ids)
            trilha.guias.add(*guias)
            
        messages.success(request, 'Guias atualizados com sucesso!')
        return redirect('trilhas_view:detalhe_trilha', trilha_id=trilha.id)
    
    # Obter todas as pessoas físicas que podem ser guias
    todos_guias = PessoaFisica.objects.all()
    guias_selecionados = trilha.guias.all()
    
    return render(request, 'trilhas_view/gerenciar_guias.html', {
        'trilha': trilha,
        'todos_guias': todos_guias,
        'guias_selecionados': guias_selecionados
    })