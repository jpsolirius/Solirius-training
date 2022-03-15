from django.shortcuts import render, redirect
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

""" def create_project(request, pk):
    project = Project.objects.get(pk=pk)
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = Project(
                title=form.cleaned_data["title"],
                description=form.cleaned_data["description"],
                technology=form.cleaned_data["technology"],
            )
            project.save()
    projects = Project.objects.filter(title=title)
    context = {
        'projects': projects,
        'form': form
    }
    return render(request, "project_form.html", context) 
 """
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

           
    
