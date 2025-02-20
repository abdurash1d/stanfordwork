from django.contrib import admin

from .models import (Job, 
                     Application,
                     JobCategory,
                     Review, 
                     JobInquiry)

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'employer', 'location', 'salary', 'created_at', 'is_active')
    list_filter = ('is_active', 'job_type', 'industry')
    search_fields = ('title', 'description', 'company')

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('candidate', 'job', 'status', 'applied_at')
    list_filter = ('status',)
    search_fields = ('candidate__username', 'job__title')
    
    
admin.site.register(JobCategory)
admin.site.register(Review)
admin.site.register(JobInquiry)
