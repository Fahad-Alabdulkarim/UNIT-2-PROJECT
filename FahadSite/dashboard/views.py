from django.shortcuts import render
from django.db.models import Q
from blog.models import Post, Comment
from main.models import Contact
from portfolio.models import Project

def dashboard(request, model_name='posts'):
    # Determine the model and item type
    if model_name == 'posts':
        Model = Post
        item_type = 'Post'
    elif model_name == 'comments':
        Model = Comment
        item_type = 'Comment'
    elif model_name == 'contacts':
        Model = Contact
        item_type = 'Contact'
    elif model_name == 'project':
        Model = Project
        item_type = 'Project'
    else:
        Model = None
        item_type = ''

    items = Model.objects.all() if Model else []

    # Handle Search
    search_query = request.GET.get('search', '')
    if search_query:
        if model_name == 'posts':
            items = items.filter(Q(title__icontains=search_query) | Q(category__icontains=search_query))
        elif model_name == 'comments':
            items = items.filter(Q(name__icontains=search_query) | Q(content__icontains=search_query))
        elif model_name == 'contacts':
            items = items.filter(Q(first_name__icontains=search_query) | Q(last_name__icontains=search_query))
        elif model_name == 'project':
            items = items.filter(Q(name__icontains=search_query) | Q(description__icontains=search_query))

    # Handle Sorting
    sort_by = request.GET.get('sort', 'id')  # Default to 'id'
    if sort_by.startswith('-'):
        sort_field = sort_by[1:]
    else:
        sort_field = sort_by

    if hasattr(Model, sort_field):  # Validate if the field exists in the model
        items = items.order_by(sort_by)

    return render(request, 'dashboard.html', {
        'items': items,
        'item_type': item_type,
        'model_name': model_name,
        'search_query': search_query,
        'current_sort': sort_by,
    })
