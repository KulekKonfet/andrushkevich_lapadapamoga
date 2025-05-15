from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('add/', views.add_project, name='add_project'),
    path('edit/<int:project_id>/', views.edit_project, name='edit_project'),
]
