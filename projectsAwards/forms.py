from django import forms
from .models import Profile, Project

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=['profile_pic','bio','contact']

class ProjectsForm(forms.ModelForm):
    class Meta:
        model = Project
        fields=['title','landing_page','description','link']