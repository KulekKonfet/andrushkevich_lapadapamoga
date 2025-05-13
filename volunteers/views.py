from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, get_user_model
from django.conf import settings
from django.http import HttpResponseRedirect
from django_telegram_login.authentication import verify_telegram_authentication
from django_telegram_login.errors import NotTelegramDataError, TelegramDataIsOutdatedError

from volunteers.models import VolunteerProject
from volunteers.forms import VolunteerProjectForm


def home(request):
    projects = VolunteerProject.objects.all()
    return render(request, 'volunteers/home.html', {'projects': projects})


@login_required
def create_project(request):
    if request.method == 'POST':
        form = VolunteerProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.organizer = request.user
            project.save()
            return redirect('home')
    else:
        form = VolunteerProjectForm()
    return render(request, 'volunteers/create_project.html', {'form': form})


@login_required
def join_project(request, project_id):
    project = VolunteerProject.objects.get(id=project_id)
    project.participants.add(request.user)
    return redirect('home')


def telegram_auth(request):
    if not request.GET.get('hash'):
        return redirect('login')

    try:
        bot_token = settings.TELEGRAM_BOT_TOKEN
        request_params = request.GET.dict()

        auth_data = verify_telegram_authentication(
            bot_token=bot_token,
            request_data=request_params
        )

        User = get_user_model()
        user, _ = User.objects.get_or_create(
            username=f"tg_{auth_data['id']}",
            defaults={
                'first_name': auth_data.get('first_name', ''),
                'last_name': auth_data.get('last_name', ''),
            }
        )

        login(request, user)
        return redirect('home')

    except (NotTelegramDataError, TelegramDataIsOutdatedError):
        return redirect('login')
