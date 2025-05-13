from django.shortcuts import render
from volunteers.models import VolunteerProject
from .forms import VolunteerProjectForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

User = get_user_model()

def project_list(request):
    projects = VolunteerProject.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})

def add_project(request):
    if request.method == 'POST':
        form = VolunteerProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = VolunteerProjectForm()
    return render(request, 'projects/add_project.html', {'form': form})

@login_required
def add_project(request):
    if request.method == 'POST':
        form = VolunteerProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.organizer = request.user
            project.save()
            return redirect('project_list')
    else:
        form = VolunteerProjectForm()
    return render(request, 'projects/add_project.html', {'form': form})