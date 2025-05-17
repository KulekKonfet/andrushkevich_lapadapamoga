from django.urls import path
from .views import home, create_project, join_project
from .views import home, create_project, join_project, profile

urlpatterns = [
    path('', home, name='home'),
    path('create_project/', create_project, name='create_project'),
    path('join_project/<int:project_id>/', join_project, name='join_project'),
    path('profile/', profile, name='profile'),
]
