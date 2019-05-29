from django.shortcuts import render, redirect, get_object_or_404
from projects.models import Project, Review
from projects.forms import AddProjectForm, ReviewForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import Http404
from projects.models import Project
from accounts.models import Profile
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import ProfileSerializer, ProjectSerializer

# Create your views here.

def home_page(request):
    
    return render(request, 'projects/projects/index.html')

@login_required
def add_project(request):
    '''
    add project function is for adding projects by user to the platform
    '''
    current_user  = request.user.profile
    form = AddProjectForm()
    if request.method == 'POST':
        form = AddProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit = False)
            project.profile = current_user
            project.save()
            return redirect(reverse('accounts:view_profile'))
    else:
        form = AddProjectForm()
        context  = {
            "form":form
            }
    return render(request, 'projects/add_project.html', context)
    
        



def display_projects(request):
    projects = Project.objects.all()
    
    context = {
        "projects":projects
    }
    
    return render(request, 'index.html', context)


# def project_details(request, pk):
#     project = Project.objects.get(pk=pk)
#     form = ReviewForm()
#     if request.method=='POST':
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             review = form.save(commit =False)
#             review.author = current_user
#             review.project = project
#             review.save()
            
#     reviews  = Rev
#             return render(request,'')

def project_detail(request, id):
    # project_details = get_object_or_404(Project, id=id)
    project_details = Project.objects.all()
    

    return render(request, 'projects/project_details.html', {'project_details':project_details})


def project_by_user(request, id):
    pass


@login_required
def add_comments(request,pk):
    project = Project.objects.filter(id=id)
    if request.method=='POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit =False)
            review.author = request.user
            review.project = project
            review.save()
            return redirect(request,'projects-details',id)
    else:
        form = ReviewForm()
        # context = {
        #     "form":form
        # }
        
    try:
        
        comments = Review.objects.filter(project_id = id)
        
    except Exception as e:
        raise Http404
        
    return render(request, 'projects/add_project.html', {"comments":comments, "form":form})
            


    
    
class ProfileAPI(APIView):
    def get(self, request, format = None):
        profiles = Profile.objects.all()
        serializers = ProfileSerializer(profiles, many=True)
        return Response(serializers.data)
        

class ProjectAPI(APIView):
    def get(self, request, format = None):
        projects= Project.objects.all()
        serializers = ProjectSerializer(projects, many=True)
        return Response(serializers.data)
    