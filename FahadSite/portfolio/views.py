from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import ProjectForm, ImageForm
from .models import Project, Images




# Create your views here.


def projects_view(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', {'projects': projects})


def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save()  
            print(request.FILES.getlist('images'))

            for img_file in request.FILES.getlist('images'):  
                image_instance = Images(project=project, images=img_file) 
                image_instance.save()
            

            return redirect('projects_view')
    else:
        form = ProjectForm()

    return render(request, 'portfolio/add_project.html', {'form': form})


def update_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects_view') 
    else:
        form = ProjectForm(instance=project)
    return render(request, 'portfolio/update_project.html', {'form': form, 'project': project})


def projects_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'portfolio/project_detail.html', {'project': project})


def delete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    project.delete()
    return redirect('projects_view')