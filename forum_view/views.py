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
   
class ForumOneView(TemplateView):
    template_name = 'forum/forumOne.html'
    def forumOne_view(request, post_id):
        post = get_object_or_404(Post, id=post_id)
        return render(request, 'forum_view/forumOne.html', {'post': post})



