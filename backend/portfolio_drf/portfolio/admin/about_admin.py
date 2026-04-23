from django.contrib import admin
from ..models.about_models import AboutInfo, Skill, Project

@admin.register(AboutInfo)
class AboutInfoAdmin(admin.ModelAdmin):
    # Helpful to see the title and subtitle in the list
    list_display = ('title', 'subtitle')
    
    def has_add_permission(self, request):
        return not AboutInfo.objects.exists()

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'percent')
    list_filter = ('category',)
    list_editable = ('percent',)
    search_fields = ('name',)    

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)   # Quickly re-arrange project priority
    search_fields = ('title',)