from cProfile import Profile
from .models import Project
from .forms import ProfileForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def home(request):
    projects=Project.objects.all()
    return render(request,'home/index.html',{'projects':projects}
    )


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
