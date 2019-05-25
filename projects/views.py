from django.shortcuts import render, redirect
from projects.models import Project

# Create your views here.

def home_page(request):
    
    return render(request, 'projects/index.html')


def add_project(request):
    pass



def display_projects(request):
    projects = Project.objects.all()
    
    return render(request, 'projects/index.html', projects)


def project_details(request, id):
    pass



    