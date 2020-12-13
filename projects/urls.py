from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.allProjects, name='allProjects'),
    path('<int:project_id>/', views.ProjDetail, name='ProjDetail'),
]
