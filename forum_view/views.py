from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Post
from django.shortcuts import get_object_or_404, redirect
from .forms import PostForm



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


def criar_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('forum')  # volta para a lista de posts
    else:
        form = PostForm()

    return render(request, 'forum/forumForm.html', {'form': form})




