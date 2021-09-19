from .models import Profile, Project,Rater,Likes
from django.contrib import admin

# Register your models here.


admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Rater)
admin.site.register(Likes)