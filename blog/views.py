from django.shortcuts import render
from .models import Post

# Create your views here.

def post_listview(request):

    post_list = Post.objects.all()
    context = {'post_list': post_list}

    return render(request, 'blog/post_list.html', context=context)