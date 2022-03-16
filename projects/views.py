from django.shortcuts import render, redirect, get_object_or_404
from projects.forms import ProjectForm
from projects.models import Project

def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)
# Create your views here.

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)

def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/projects/')
    else:
        form = ProjectForm()
    return render(request, 'project_form.html', {
        'form': form})

def edit_project(request, pk):
    project = Project.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('/projects')
    else:
        form = ProjectForm(instance=project)
    context = {
        'form': form,
    }
    return render(request, 'edit_project.html', context)

def delete_project(request, pk):
    project = Project.objects.get(pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('/projects')
    context = {'item': project}
    return render(request, 'delete_project.html', context)