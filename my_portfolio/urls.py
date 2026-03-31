from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/<slug:slug>/', views.project_detail, name='project_detail'),
    path('resumes/<slug:slug>/', views.resume_detail, name='resume_detail'),
]
