from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, get_user_model
from django.conf import settings
from django_telegram_login.authentication import verify_telegram_authentication
from django_telegram_login.errors import NotTelegramDataError, TelegramDataIsOutdatedError
from volunteers.models import VolunteerProject
from volunteers.forms import VolunteerProjectForm
from django.contrib.auth.forms import UserCreationForm


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
    project = get_object_or_404(VolunteerProject, id=project_id)
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
    

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('project_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def telegram_login(request):
    try:
        if request.GET:
            bot_token = settings.TELEGRAM_BOT_TOKEN
            user_data = verify_telegram_authentication(bot_token=bot_token, request_data=request.GET.dict())
            if user_data:
                User = get_user_model()
                username = user_data.get("username") or f"tg_{user_data['id']}"
                user, created = User.objects.get_or_create(username=username)
                login(request, user)
    except (NotTelegramDataError, TelegramDataIsOutdatedError):
        pass
    return redirect('project_list')
