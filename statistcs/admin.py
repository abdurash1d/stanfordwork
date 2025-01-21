from django.contrib import admin
from .models import JobPostingAnalytics

@admin.register(JobPostingAnalytics)
class JobPostingAnalyticsAdmin(admin.ModelAdmin):
    list_display = ('job', 'view_count', 'update_count', 'last_updated_at')
    list_filter = ('last_updated_at',)
    search_fields = ('job__title',)
