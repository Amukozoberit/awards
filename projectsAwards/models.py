from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
# Create your models here.
from django.db.models.signals import post_save
from django.core.validators import MinValueValidator, MaxValueValidator

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic=models.ImageField(upload_to='profile_pics/', blank=True)
    bio=models.TextField(max_length='50',blank=True)
    # projects=models.ForeignKey()
    contact=models.TextField(max_length=50,blank=True)



@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

# @receiver(post_save,sender=User)
# def save_user_profile(sender,instance,created,**kwargs):
#     if created:
#         Profile.objects.create(user=instance)

class Project(models.Model):
    title=models.TextField(max_length=50)
    landing_page=models.ImageField(upload_to='landing_pages/')
    description=models.TextField(max_length=1000)
    link=models.URLField(max_length=200,blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    users=models.ForeignKey(User,on_delete=models.CASCADE)


class Rater(models.Model):
    users=models.ForeignKey(User,on_delete=models.CASCADE)
    projects=models.ForeignKey(Project,on_delete=models.CASCADE)
    design=models.IntegerField()
    usability=models.IntegerField()
    content=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    average=models.FloatField(blank=True)




