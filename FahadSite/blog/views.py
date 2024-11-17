from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from django.utils import timezone
from .forms import PostForm, CommentForm


# Create your views here.



def blog_view(request):
    posts = Post.objects.order_by('-published_at')
    return render(request, 'blog.html', {'posts': posts})


def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("blog")
    else:
        form = PostForm()
    return render(request, "add_post.html", {"form": form})

def update_post(request, blog_id):
    post = get_object_or_404(Post, pk=blog_id)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("blog")
    else:
        form = PostForm(instance=post)
    return render(request, "update_post.html", {"form": form, "post": post})

def posts_detail(request, blog_id):
    post = get_object_or_404(Post, pk=blog_id)
    comments = post.comments.all()
    if request.method == "POST":
        if "comment" in request.POST:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.save()
                return redirect("posts_detail", blog_id=post.id)
        elif "like" in request.POST:
            post.likes += 1
            post.save()
            return redirect("posts_detail", blog_id=post.id)
    else:
        comment_form = CommentForm()
    return render(request, 'posts_detail.html', {"post": post, "comments": comments, "comment_form": comment_form})


def delete_post(request, blog_id):
    post = get_object_or_404(Post, pk=blog_id)
    post.delete()
    return redirect('blog')

def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    blog_id = comment.post.id
    comment.delete()
    return redirect("posts_detail", blog_id=blog_id)
