from django.contrib import admin
from .models import Doctor

# Register the Doctor model with custom admin fields and settings
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    # Specify columns for the list view
    list_display = ('name', 'specialization', 'email', 'contact_number')
    
    # Add search capability
    search_fields = ('name', 'specialization', 'email')
    
    # Enable filtering in the right sidebar
    list_filter = ('specialization',)
    
    # Group fields into logical sections in the detail view
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'specialization')
        }),
        ('Contact Details', {
            'fields': ('email', 'contact_number', 'address')
        }),
    )
