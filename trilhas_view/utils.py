from django.shortcuts import redirect
from django.contrib import messages

def admin_required(view_func):
    """
    Decorador que verifica se o usuário é administrativo (superuser ou staff).
    Redireciona usuários não logados para o login e usuários sem permissão
    para a lista de trilhas com uma mensagem de erro.
    """
    def wrapper(request, *args, **kwargs):
        # Verifica se o usuário está logado
        if not request.user.is_authenticated:
            # Redireciona para a página de login, salvando o URL original
            # Assumindo que você tem uma view de login em 'home_view:login'
            return redirect('home_view:login')
        
        # Verifica se o usuário é administrativo
        if not (request.user.is_superuser or request.user.is_staff):
            # Adiciona uma mensagem de erro
            messages.error(
                request, 
                'Você não tem permissão para realizar esta operação. Acesso restrito ao setor administrativo.'
            )
            # Redireciona para a lista de trilhas
            return redirect('trilhas_view:lista_trilhas')
        
        # Se o usuário tem permissão, continua com a view original
        return view_func(request, *args, **kwargs)
    
    return wrapper