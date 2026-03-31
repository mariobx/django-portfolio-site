from django.contrib import admin
from .models import Project, Resume, ProjectImage

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'slug')
    list_editable = ('order',)
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProjectImageInline]

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('label', 'order', 'slug')
    list_editable = ('order',)
    prepopulated_fields = {'slug': ('label',)}
