from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from django.http import HttpResponse
from .models import Post
from .forms import PostForm

def index(request): 
    return HttpResponse("You're at Posts index.")

def post_list(request):
    posts = Post.objects.all().order_by('-dateOfCreation')  # Ordering by creation date
    return render(request, 'posts/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/post_detail.html', {'post': post})

def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/edit_post.html', {'form': form})

@require_POST
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')


