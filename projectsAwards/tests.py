from datetime import datetime
from pydoc import describe
import unittest
from django.test import TestCase
from django.db import models
from django.contrib.auth.models import User
from .models import Likes, Profile, Project, Rater
import tempfile
# Create your tests here.


class ProfileTestClass(TestCase):

    def setUp(self):
        user=User(username="peter",email='mwasheberit@gmail.com',password='parapara')
        image=tempfile.NamedTemporaryFile().name
        self.new_profile=Profile(user=user,bio='developer',contact='0721222536')
        self.new_profile.profile_pic=image
        # self.new_profile.save()
    def tearDown(self):
        User.objects.all().delete()
        Profile.objects.all().delete()
        
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))




   
class ProjectTestCase(TestCase):
    def setUp(self):
        user=User(username="peter",email='mwasheberit@gmail.com',password='parapara')
        image=tempfile.NamedTemporaryFile().name
        self.new_project=Project(description='news application',link='https://mail.google.com/mail/u/3/#inbox',pub_date=datetime.now,users=user)
        self.new_project.landing_page=image
    def tearDown(self):
        User.objects.all().delete()
        Project.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_project,Project))

class RaterTestCase(TestCase):
    def setUp(self):
        user=User(username="peter",email='mwasheberit@gmail.com',password='parapara')
        image=tempfile.NamedTemporaryFile().name
        self.new_project=Project(description='news application',link='https://mail.google.com/mail/u/3/#inbox',pub_date=datetime.now,users=user)
        self.new_project.landing_page=image
        self.new_rate=Rater(design=5,usability=5,content=5,average=(5+5+5)/3)
        self.new_rate.projects=self.new_project
        self.new_rate.users=user

    def tearDown(self):
        User.objects.all().delete()
        Project.objects.all().delete()
        Rater.objects.all().delete()
    def test_instance(self):
        self.assertTrue(isinstance(self.new_rate,Rater))

class LikesTestClass(TestCase):
    def setUp(self):
        image=tempfile.NamedTemporaryFile().name
        user=User(username="peter",email='mwasheberit@gmail.com',password='parapara')    
        self.new_project=Project(description='news application',link='https://mail.google.com/mail/u/3/#inbox',pub_date=datetime.now,users=user)
        self.new_project.landing_page=image
        self.new_like=Likes()
        self.new_like.user=user
        self.new_like.project=self.new_project

    def tearDown(self):
        User.objects.all().delete()
        Project.objects.all().delete()
        Rater.objects.all().delete()
    def test_instance(self):
        self.assertTrue(isinstance(self.new_like,Likes))