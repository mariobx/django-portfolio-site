from django.contrib import admin
from .models import Project, ProjectImage, Resume, HomePage

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1
    fields = ('order', 'image', 'video_url', 'blocked_embed', 'caption')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'slug')
    list_editable = ('order',)
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProjectImageInline]

    class Media:
        js = ('js/admin_toggle.js',)

@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not HomePage.objects.exists()

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('label', 'order', 'slug')
    list_editable = ('order',)
    prepopulated_fields = {'slug': ('label',)}
