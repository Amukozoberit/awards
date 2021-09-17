from django.conf import settings
from django.conf.urls import url
from . import views
from django.conf.urls.static import static

urlpatterns=[
 url(r'^$',views.home,name='indexpage'),
#  url(r'profile',views.update_profile,name='profilepage')]
]



