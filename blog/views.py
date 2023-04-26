from typing import Any, Optional
from django.db import models
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Blog
from .forms import NewPostForm
from django.urls import reverse, reverse_lazy
from django.views import generic

# def posts_view(request):
#     posts = Blog.objects.filter(status='pub').order_by()
#     return render(request, 'posts_view.html', context={'posts':posts})

class PostView(generic.ListView):
    model = Blog
    context_object_name = 'posts'
    template_name = 'posts_view.html'
    
    def get_queryset(self):
        return Blog.objects.filter(status='pub')
    

# def detail_view(request, pk):
#     posts = get_object_or_404(Blog, pk=pk)
#     return render(request, 'detail_view.html', context={'posts':posts})

class DetailView(generic.DetailView):
    model = Blog
    context_object_name = 'posts'
    template_name = 'detail_view.html'



# def create_post(request):
#     form = NewPostForm(request.POST or None)
    
#     if form.is_valid():
#         form.save()
#         return redirect('posts_view')
#     # if request.method == 'POST':
#     #     form = NewPostForm(request.POST)
#     #     if form.is_valid():
#     #         form.save()
#     #         return redirect('posts_view')
#     # else:
#     #     form = NewPostForm()
        
#     return render(request, 'create_post.html', context={'form':form})

class CreatePost(generic.CreateView):
    template_name = 'create_post.html'
    context_object_name = 'form'
    form_class = NewPostForm
    success_url = reverse_lazy('posts_view')
    


# def edit_post(request, pk):
#     model = get_object_or_404(Blog, pk=pk)
#     form = NewPostForm(request.POST or None , instance=model)
    
#     if form.is_valid():
#         form.save()
#         return redirect('detail_view',pk)
    
#     return render(request, 'edit_post.html', context={'form':form})
    
class EditPost(generic.UpdateView):
    template_name = 'edit_post.html'
    form_class = NewPostForm
    model = Blog

    
    
def del_post(request, pk):
    model = get_object_or_404(Blog, pk=pk)
    model.delete()
    return redirect('posts_view')

# class DelPost(generic.DeleteView):
#     model = Blog
    