from django.shortcuts import render
from blog.models import Post, Comment
from main.models import Contact
from portfolio.models import Project

# Create your views here.






def dashboard(request, model_name='posts'):
    if model_name == 'posts':
        items = Post.objects.all()
        item_type = 'Post'
    elif model_name == 'comments':
        items = Comment.objects.all()
        item_type = 'Comment'
    elif model_name == 'contacts':
        items = Contact.objects.all()
        item_type = 'Contact'
    elif model_name == 'projects':
        items = Project.objects.all()
        item_type = 'Project'
    else:
        items = []
        item_type = ''

    return render(request, 'dashboard.html', {
        'items': items,
        'item_type': item_type,
        'model_name': model_name,
    })
