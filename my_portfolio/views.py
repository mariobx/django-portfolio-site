from django.shortcuts import render, get_object_or_404
from django.http import FileResponse, HttpResponse
from django.conf import settings
import os
from .models import Project, Resume, HomePage

def home(request):
    home_content = HomePage.objects.first()
    return render(request, 'my_portfolio/home.html', {'home_content': home_content})

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'my_portfolio/project_detail.html', {'project': project})

def resume_detail(request, slug):
    resume = get_object_or_404(Resume, slug=slug)
    file_path = os.path.join(settings.BASE_DIR, 'static', 'pdf', resume.file_path)
    
    # We use HttpResponse instead of FileResponse so the static export tool can read the content
    with open(file_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/pdf')
        # This tells the browser to display it in-line
        response['Content-Disposition'] = f'inline; filename="{resume.file_path}"'
        return response

# Context processor for dropdowns
def portfolio_context(request):
    return {
        'all_projects': Project.objects.all(),
        'all_resumes': Resume.objects.all(),
    }
