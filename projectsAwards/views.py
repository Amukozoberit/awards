from django.db.models import Avg
from django.db.models import Count
from .models import Likes, Project,Profile, Rater
from .forms import ProfileForm, ProjectsForm, RatesForm
from django.http import HttpResponse, HttpResponseRedirect
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
    users=User.objects.all()
    # rates=Rater.objects.filter(projects=id)
    
    # average=Rater.get_avg(rates)
    rates=Rater.objects.values('projects').annotate(dcount=Count('projects')).order_by()
    print(rates)
    avgs=[]
    for r in rates:
         print(r['projects'])
         rat=Rater.objects.filter(projects=r['projects'])
         average=Rater.get_avg(rat)
        #  print(average)
         avgs.append(average['average__avg'])
    print(f'{max(avgs)} avg')
    print(rates)
    for rates in rates:
        rat=Rater.objects.filter(projects=rates['projects'])
        average=Rater.get_avg(rat)
        print(average)
        if average['average__avg']==max(avgs):
         max_avg=rates['projects']



    forday=Project.objects.get(id=max_avg)
    print(forday)
    print(max_avg)
    likes=Likes.objects.filter(project_id=max_avg)



    
    # rates=Rater.objects.filter(average=7.333333333333333)
    # print(rates)
    
    #     projects=Project.objects.get(id=rates['projects'])
    #     for projects in projects:
    #         print(projects)
    return render(request,'home/index.html',{'users':users,'projects':projects,'forday':forday,'likes':likes}
    )
   
def allprojects(request):
    projects=Project.objects.all()
    # users=User.objects.all()
    return render(request,'home/allprojects.html',{'projects':projects}
    )

def addproject(request):
    currentu=request.user
    
   
    form=ProjectsForm()
    

    if request.method=='POST':
                form=ProjectsForm(request.POST,request.FILES)
                if form.is_valid():
                    project=form.save(commit=False)
                    project.users=currentu
                    
                    project.save()
                    return redirect('/')
    else:
                    form=ProjectsForm()

            # rates=Rater.objects.all()
    return render(request,'home/newproject.html' ,{'form':form})


def addrate(request,id):
    currentu=request.user
    currentP=Project.objects.get(id=id)
    allrates=Rater.objects.filter(projects=id)
    form=RatesForm()
    all=[]
    for alr in allrates:
       all.append(alr.users.id)
       print(f'{all}id')
    if not request.user.id in all:
        if request.method=='POST':
                    form=RatesForm(request.POST)
                    if form.is_valid():
                        rate=form.save(commit=False)
                        rate.projects=currentP
                        rate.users=currentu
                        rate.average=((rate.design)+(rate.usability)+(rate.content))/3
                        rate.save()
                        return redirect('/')
        else:
                        form=RatesForm()
                        # return redirect('/')

                # rates=Rater.objects.all()
        return render(request,'home/newrate.html' ,{'form':form,'id':id})
        
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def editProfile(request,id):
    prof=Profile.objects.get(id=id)
    form=ProfileForm()
    if prof.user.id ==request.user.id:
        return render(request,'home/updateprofile.html',{'form':form,'id':id})


# @login_required
# @transaction.atomic
def update_profile(request):
        if request.method == 'POST':
            print('not yet')
            # user_form = UserForm(request.POST, instance=request.user)
            profile_form = ProfileForm(request.POST, request.FILES,instance=request.user.profile)
            if  profile_form.is_valid():
                # user_form.save()
                print('yes')
                profile_form.save()
                messages.success(request, ('Your profile was successfully updated!'))
                return redirect('/')
            else:
                print('nono')
                messages.error(request, ('Please correct the error below.'))
        else:
            print('no')
            # user_form = UserForm(instance=request.user)
            profile_form = ProfileForm(instance=request.user.profile)
        return render(request, 'home/updateprofile.html', {
        # 'user_form': user_form,
        'form': profile_form
    })
    
def search_results(request):
    if 'projects' in request.GET and request.GET['projects']:
        search_term=request.GET.get('projects')
        searched_project=Project.search_by_title(search_term)
        message=f"{search_term}"

        return render(request,'home/search.html',{"message":message,'search_project':searched_project})


def single_project(request,id):
    project=Project.objects.get(id=id)
    rates=Rater.objects.filter(projects=id)
    
    average=Rater.get_avg(rates)
    average=average['average__avg']
    
    lik=Likes.objects.filter(project_id=id)
    print(f'{lik} likes')

    
    
    return render(request,'home/single_project.html',{'project':project,'rates':rates,'average':average,'likes':lik})

def likeproject(request,id):
    postTobeliked=Project.objects.get(id=id)
    currentUser=User.objects.get(id=request.user.id)
    postowner=User.objects.get(id=postTobeliked.users.id)
    print(currentUser)
    likes=Likes.objects.filter(id=id)
    likeToadd=Likes(user=currentUser,project=postTobeliked)
    all=[]
    for alr in likes:
       all.append(alr.user.id)
       print(f'{all}id')
    if not request.user.id in all:
        if postowner.id ==currentUser.id :
                print('yer')
                # alert('cant like own picture')
                # folowerToremove=Followers(name=request.user.username,user_id=userTobefollowed.id,follower_id=request.user.url)
                # folowerToremove.remove(currentUser)
        else:   
                print('no')
                # likeToadd=LikeClass(user_id=currentUser,post_id=postTobeliked)
                print(likeToadd)
                likeToadd.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))




def single_profile(request,id):
    prof=User.objects.get(id=id)
    projects=Project.objects.filter(users=1)
  
    return render(request,'profile/profile.html',{'profile':prof,'projects':projects,})
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


