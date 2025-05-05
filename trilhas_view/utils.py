from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse
from functools import wraps

def admin_required(view_func):
    """
    Decorador que verifica se o usuário é superuser ou staff do Django.
    Redireciona usuários não autorizados com mensagens apropriadas.
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        # Verificar se o usuário está logado e é superuser ou staff
        if not request.user.is_authenticated:
            # Redirecionar para a página de login
            next_url = request.get_full_path()
            login_url = f"{reverse('admin:login')}?next={next_url}"
            return redirect(login_url)
        
        # Verificar se o usuário é superuser ou staff
        if not (request.user.is_superuser or request.user.is_staff):
            messages.error(
                request, 
                'Você não tem permissão para realizar esta operação. Acesso restrito ao setor administrativo.'
            )
            return redirect('trilhas_view:lista_trilhas')
        
        return view_func(request, *args, **kwargs)
    
    return wrapper