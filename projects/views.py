from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from volunteers.models import VolunteerProject
from .forms import VolunteerProjectForm

def project_list(request):
    projects = VolunteerProject.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})

@login_required
def add_project(request):
    if request.method == 'POST':
        form = VolunteerProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.organizer = request.user
            project.save()
            return redirect('projects:project_list')
    else:
        form = VolunteerProjectForm()
    return render(request, 'projects/add_project.html', {'form': form})

@login_required
def edit_project(request, project_id):
    project = get_object_or_404(VolunteerProject, id=project_id)

    if request.user != project.organizer:
        return HttpResponseForbidden("У вас нет прав для редактирования этого проекта.")

    if request.method == 'POST':
        form = VolunteerProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects:project_list')
    else:
        form = VolunteerProjectForm(instance=project)

    return render(request, 'projects/edit_project.html', {'form': form})

@login_required
def join_project(request, project_id):
    project = get_object_or_404(VolunteerProject, id=project_id)

    if request.method == 'POST':
        project.participants.add(request.user)
        return redirect('projects:project_list')

    return render(request, 'projects/join_project.html', {'project': project})