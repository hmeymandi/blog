from django.shortcuts import render,redirect
from .models import Post
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .forms import NewPostForm
from django.views import generic

from django.urls import reverse_lazy
# Create your views here.

class PostListView(generic.ListView):
    
    template_name = 'blog/post_list.html'
    context_object_name = 'post_list'
    
    def get_queryset(self):
        return Post.objects.filter(status="pub").order_by('-date_modified')

    

class Post_detail_view(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post_detail_view'


class Create_PostView(generic.CreateView):
    form_class = NewPostForm
    template_name = 'blog/add_post.html'


class Update_PostView(generic.UpdateView):
    model = Post
    form_class = NewPostForm
    template_name = 'blog/add_post.html'


class Delete_PostView(generic.DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    
    def get_success_url(self):
        return reverse_lazy('post_listview')

# def post_listview(request):

#     post_list = Post.objects.filter(status="pub").order_by('-date_modified')
#     context = {'post_list': post_list}

#     return render(request, 'blog/post_list.html', context=context)

# def post_detail_view(request,pk):

#     post_detail_view = get_object_or_404(Post , pk=pk)
#     context = {'post_detail_view': post_detail_view}

#     return render(request, 'blog/post_detail.html',context=context)

# def create_post (request):
#     if request.method == 'POST':
#         form = NewPostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('post_listview')

        
#     else:
#         form = NewPostForm()

#         return render(request, 'blog/add_post.html',context={'form' : form})
    
# def post_detail_update(request,pk):

#     post = get_object_or_404(Post, pk=pk)
#     form = NewPostForm(request.POST or None ,instance=post)
#     if form.is_valid():
#         form.save()
#         return redirect('post_listview')
        

#     return render(request, 'blog/add_post.html', {'form': form})


def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post_listview')

    return render(request, 'blog/post_delete.html', {'post': post})

