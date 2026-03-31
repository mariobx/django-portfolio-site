from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    short_description = models.CharField(max_length=300, blank=True, help_text="A brief one-sentence summary (italicized on page).")
    description = models.TextField()
    github_url = models.URLField(blank=True, null=True)
    main_image = models.ImageField(upload_to='projects/main/', blank=True, null=True)

    def __str__(self):
        return self.title

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='gallery', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projects/gallery/')
    caption = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"Image for {self.project.title}"

class Resume(models.Model):
    label = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    file_path = models.CharField(max_length=255) # Relative to static/pdf/

    def __str__(self):
        return self.label
