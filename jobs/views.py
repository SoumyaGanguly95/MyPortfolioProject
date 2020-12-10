from django.shortcuts import render
from .models import Job
from projects.models import Project


# Create your views here.
def home(request):
    jobs = Job.objects
    project = Project.objects
    return render(request, 'jobs/home.html', {'jobs': jobs, 'projects': project})
