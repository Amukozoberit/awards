from django import forms
from .models import Profile, Project, Rater

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=['profile_pic','bio','contact']

class ProjectsForm(forms.ModelForm):
    class Meta:
        model = Project
        fields=['title','landing_page','description','link']


class RatesForm(forms.ModelForm):
    class Meta:
        model = Rater
        fields=['design','usability','content']