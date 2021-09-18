
from re import search
from .models import Project,Profile, Rater
from .forms import ProfileForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer,ProjectSerializer
def home(request):
    projects=Project.objects.all()
    return render(request,'home/index.html',{'projects':projects}
    )



def search_results(request):
    if 'projects' in request.GET and request.GET['projects']:
        search_term=request.GET.get('projects')
        searched_project=Project.search_by_title(search_term)
        message=f"{search_term}"

        return render(request,'home/search.html',{"message":message,'search_project':searched_project})


def single_project(request,id):
    project=Project.objects.get(id=id)
    rates=Rater.objects.get(id=id)
    avg=(rates.design)+(rates.usability)+(rates.content)
    return render(request,'home/single_project.html',{'project':project,'rates':rates,'avg_rates':avg})


def single_profile(request,id):
    prof=User.objects.get(id=id)
    projects=Project.objects.filter(users=1)
    return render(request,'profile/profile.html',{'profile':prof,'projects':projects})
# @login_required

# def update_profile(request):
#     if request.method == 'POST':
#         # user_form = UserForm(request.POST, instance=request.user)
#         profile_form = ProfileForm(request.POST, instance=request.user.profile)
#         if profile_form.is_valid():
#             # user_form.save()
#             profile_form.save()
#             messages.success(request,('Your profile was successfully updated!'))
#             return redirect('/')
#         else:
#             messages.error(request,('Please correct the error below.'))
#     else:
#         # user_form = UserForm(instance=request.user)
#         profile_form = ProfileForm(instance=request.user.profile)
#     return render(request, 'profile/profile.html', {
#         # 'user_form': user_form,
#         'profile_form': profile_form
#     })
class ProfileList(APIView):
    def get(self,request,format=None):
        all_merch=Profile.objects.all()
        serializers=ProfileSerializer(all_merch,many=True)
        return Response(serializers.data)


class ProjectList(APIView):
    def get(self,request,format=None):
        all_merch=Project.objects.all()
        serializers=ProjectSerializer(all_merch,many=True)
        return Response(serializers.data)