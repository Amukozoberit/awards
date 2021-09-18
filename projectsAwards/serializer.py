from rest_framework import serializers
from .models import Profile, Project



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=('user','profile_pic','bio','contact')



class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields=('title','landing_page','description','link','pub_date','users')

