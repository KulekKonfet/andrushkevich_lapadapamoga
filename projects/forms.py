from django import forms
from volunteers.models import VolunteerProject

class VolunteerProjectForm(forms.ModelForm):
    class Meta:
        model = VolunteerProject
        fields = ['title', 'description', 'category']
