from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Post
from django.shortcuts import get_object_or_404, redirect
from .forms import PostForm
from django.contrib.auth.decorators import login_required


################################################ enzo enzo




# Create your views here.
class ForumView(TemplateView):
    template_name = 'forum/forum.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context
    
 
def forum(request):
    posts = Post.objects.all()
    return render(request, 'forum/forum.html', {'posts': posts})



def forumOne(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'forum/forumOne.html', {'post': post})

def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.likes += 1
    post.save()
    return redirect('forum_view:forum_one', pk=post.pk)





def criar_post(request):
    if not request.session.get('is_authenticated'):
        return redirect('/login/?next=/forum/formulario/')

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)

            # Aqui você precisa buscar o "autor"
            from django.contrib.auth.models import User
            try:
                user = User.objects.get(email=request.session.get('user_email'))
                post.autor = user
            except User.DoesNotExist:
                return HttpResponse("Usuário não encontrado no sistema de autenticação.")

            post.save()
            return redirect('forum_view:forum')
    else:
        form = PostForm()

    return render(request, 'forum/forumForm.html', {'form': form})




def meus_posts(request):
    posts = Post.objects.filter(autor=request.user).order_by('-criado_em')
    return render(request, 'forum/meus_posts.html', {'posts': posts})




