from django.conf import settings
from django.conf.urls import url
from . import views
from django.conf.urls.static import static

urlpatterns=[
 url(r'^$',views.home,name='indexpage'),
url(r'^api/profiles/$', views.ProfileList.as_view()),
url(r'^api/projects/$', views.ProjectList.as_view()),
url('search/', views.search_results, name='search_results'),
url('single_project/(\d+)', views.single_project, name='single_project'),
url('profile/(\d+)', views.single_profile, name='profile')
#  url(r'profile',views.update_profile,name='profilepage')]
]



