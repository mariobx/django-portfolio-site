from django.shortcuts import render, get_object_or_404
from django.http import FileResponse
from django.conf import settings
import os
from .models import Project, Resume

def home(request):
    return render(request, 'my_portfolio/home.html')

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'my_portfolio/project_detail.html', {'project': project})

def resume_detail(request, slug):
    resume = get_object_or_404(Resume, slug=slug)
    file_path = os.path.join(settings.BASE_DIR, 'static', 'pdf', resume.file_path)
    return FileResponse(open(file_path, 'rb'), content_type='application/pdf')

# Context processor for dropdowns
def portfolio_context(request):
    return {
        'all_projects': Project.objects.all(),
        'all_resumes': Resume.objects.all(),
    }
