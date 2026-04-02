from django.urls import path
from django_distill import distill_path
from . import views
from .models import Project, Resume

def get_all_projects():
    for project in Project.objects.all():
        yield {'slug': project.slug}

def get_all_resumes():
    for resume in Resume.objects.all():
        yield {'slug': resume.slug}

def get_index():
    return None

urlpatterns = [
    distill_path('', views.home, name='home', distill_func=get_index),
    distill_path('projects/<slug:slug>/', views.project_detail, name='project_detail', distill_func=get_all_projects),
    # Added .pdf extension to force the export tool to name the files correctly
    distill_path('resumes/<slug:slug>.pdf', views.resume_detail, name='resume_detail', distill_func=get_all_resumes),
]
