from django import forms
from volunteers.models import VolunteerProject


class VolunteerProjectForm(forms.ModelForm):
    class Meta:
        model = VolunteerProject
        fields = ['title', 'description', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название проекта'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Описание проекта'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Название проекта',
            'description': 'Описание',
            'category': 'Категория',
        }
