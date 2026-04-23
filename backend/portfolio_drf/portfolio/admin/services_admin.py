from django.contrib import admin
from ..models.services_models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    # Displays the main info at a glance
    list_display = ('title', 'icon_name', 'order')
    
    # Allows you to change the display order directly in the list
    list_editable = ('order',)
    
    # Adds a search bar to quickly find specific services
    search_fields = ('title', 'description', 'icon_name')
    
    list_filter = ('icon_name',)

    fieldsets = (
        ('Service Details', {
            'fields': ('title', 'description')
        }),
        ('Aesthetics & Ranking', {
            'fields': ('icon_name', 'order'),
            'description': 'Use Lucide-React icon names (e.g., Code, Server, Database).'
        }),
    )