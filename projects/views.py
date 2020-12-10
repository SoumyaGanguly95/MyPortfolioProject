from django.shortcuts import render, get_object_or_404

from .models import Project


# Create your views here.
def allProjects(request):
    project = Project.objects
    return render(request, 'MyPortfolio/jobs/templates/jobs/home.html', {'project': project})


def detail(request, project_id):
    detailprojects = get_object_or_404(Project, pk=project_id)
    return render(request, 'projects/projectDetail.html', {'project': detailprojects})
