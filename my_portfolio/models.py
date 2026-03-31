from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    order = models.PositiveIntegerField(default=0, help_text="Lower numbers appear first in the menu.")
    short_description = models.CharField(max_length=300, blank=True)
    description = models.TextField()
    github_url = models.URLField(blank=True, null=True)
    pypi_url = models.URLField(blank=True, null=True, verbose_name="PyPI URL")
    main_image = models.ImageField(upload_to='projects/main/', blank=True, null=True)

    class Meta:
        ordering = ['order', 'title']

    def __str__(self):
        return self.title

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='gallery', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projects/gallery/', blank=True, null=True)
    caption = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"Image for {self.project.title}"

class Resume(models.Model):
    label = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    order = models.PositiveIntegerField(default=0)
    file_path = models.CharField(max_length=255) # Relative to static/pdf/

    class Meta:
        ordering = ['order', 'label']

    def __str__(self):
        return self.label
