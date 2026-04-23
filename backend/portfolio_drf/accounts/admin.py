from django.contrib import admin
from .models import ContactInquiry

@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    
    # Sidebar filters ko lagi
    list_filter = ('created_at',)
    
    # for search box 
    search_fields = ('name', 'email', 'message')
    ordering = ('-created_at',)