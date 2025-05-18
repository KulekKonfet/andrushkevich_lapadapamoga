from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from volunteers.models import VolunteerProject
from volunteers.models import VolunteerProfile


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

class CustomUserCreationForm(UserCreationForm):
    role = forms.ChoiceField(choices=VolunteerProfile.ROLE_CHOICES, label="Роль", widget=forms.Select(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "role")

    def save(self, commit=True):
        user = super().save(commit)
        role = self.cleaned_data["role"]
        user.volunteerprofile.role = role
        if commit:
            user.volunteerprofile.save()
        return user
    

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }
        