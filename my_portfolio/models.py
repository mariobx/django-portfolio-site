from django.db import models
from django.core.exceptions import ValidationError
import yt_dlp
import re

class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    order = models.PositiveIntegerField(default=0, help_text="Lower numbers appear first.")
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
    image = models.ImageField(upload_to='projects/gallery/', blank=True, null=True, help_text="Upload an image/GIF.")
    video_url = models.URLField(blank=True, null=True, help_text="OR paste a YouTube URL.")
    video_id = models.CharField(max_length=20, blank=True, null=True, editable=False)
    blocked_embed = models.BooleanField(default=False, help_text="Check this if YouTube blocks embedding.")
    caption = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = "Project Media"
        verbose_name_plural = "Project Media"

    def clean(self):
        if self.image and self.video_url:
            raise ValidationError("Please provide either an image OR a video URL, not both.")
        if not self.image and not self.video_url:
            raise ValidationError("You must provide an image or a video URL.")

    def save(self, *args, **kwargs):
        if self.video_url:
            ydl_opts = {'quiet': True, 'extract_flat': True, 'skip_download': True, 'socket_timeout': 5}
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(self.video_url, download=False)
                    self.video_id = info.get('id')
                    if self.video_id:
                        self.video_url = f"https://www.youtube.com/watch?v={self.video_id}"
            except Exception:
                match = re.search(r'(?:v=|\/)([0-9A-Za-z_-]{11}).*', self.video_url)
                if match: self.video_id = match.group(1)
        else:
            self.video_id = None
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Media for {self.project.title}"

class HomePage(models.Model):
    name = models.CharField(max_length=100, default="Mario Marku")
    description = models.TextField(help_text="The main text on your home page. HTML is allowed.")

    class Meta:
        verbose_name = "Home Page Content"
        verbose_name_plural = "Home Page Content"

    def __str__(self):
        return "Home Page Configuration"

class Resume(models.Model):
    label = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    order = models.PositiveIntegerField(default=0)
    file_path = models.CharField(max_length=255)

    class Meta:
        ordering = ['order', 'label']

    def __str__(self):
        return self.label
