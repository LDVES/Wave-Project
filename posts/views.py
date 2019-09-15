from django.shortcuts import render
# views.py
from django.views.generic import ListView
from posts.models import Post

class PostsList(ListView):
    model = Post
    context_object_name = 'posts'
    template_name='posts/post_list.html'
    ordering = ['-created_at']
    paginate_by = 5
    queryset = Post.objects.all()
# Create your views here.

