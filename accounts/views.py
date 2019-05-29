from django.shortcuts import render, redirect
from accounts.forms import (
    RegistrationForm, EditProfileForm)
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from projects.models import Project
from .models import Profile
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

# Create your views here.

# def home(request):
#     title = "Home"
#     return render(request, 'accounts/home.html', {"title":title})



def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts')
    else:
        form = RegistrationForm()
        context = {
            'form':form
        }
        
    return render(request,'accounts/register_form.html',context)
    
    
    
    
# @login_required   
# def view_profile(request):
#     context  = {"user":request.user}
#     return render(request, 'accounts/profile.html', context)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance = request.user)
        if form.is_valid:
            form.save()
            return redirect('/accounts/profile')
        
    else:
        form = EditProfileForm(instance  = request.user)
        context = {
            "form":form
        }
        return render(request, 'accounts/edit_profile.html', context)
    

@login_required          
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user = request.user)
        if form.is_valid:
            form.save()
            return redirect('/accounts/profile')
        
    else:
        form = PasswordChangeForm(user  = request.user)
        context = {
            "form":form
        }
        return render(request, 'accounts/change_password.html', context)
    
    
@login_required
def user_profile(request):
    current_user = request.user
    projects = Project.objects.filter(profile = current_user.profile)
    print(current_user.profile)

    try:
        profile = Profile.objects.get(user=current_user)
        
    except ObjectDoesNotExist:
        return redirect('register')

    context = { 
               'profile':profile,
               'projects':projects,
               'current_user':current_user
               }
    return render(request,'accounts/profile.html',context)



def logout(request):
    pass
    