from django.contrib import admin
from .models import JobViewLog, UserActivityLog, JobApplicationStats, AdminDashboardSettings, JobPostingAnalytics

@admin.register(JobViewLog)
class JobViewLogAdmin(admin.ModelAdmin):
    list_display = ('job', 'viewer', 'viewed_at')
    list_filter = ('viewed_at',)
    search_fields = ('job__title', 'viewer__username')

@admin.register(UserActivityLog)
class UserActivityLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'timestamp', 'ip_address')
    list_filter = ('timestamp',)
    search_fields = ('user__username', 'action')

@admin.register(JobApplicationStats)
class JobApplicationStatsAdmin(admin.ModelAdmin):
    list_display = ('job', 'total_applications', 'last_updated')
    list_filter = ('last_updated',)
    search_fields = ('job__title',)

@admin.register(AdminDashboardSettings)
class AdminDashboardSettingsAdmin(admin.ModelAdmin):
    list_display = ('key', 'value')
    search_fields = ('key',)

@admin.register(JobPostingAnalytics)
class JobPostingAnalyticsAdmin(admin.ModelAdmin):
    list_display = ('job', 'view_count', 'update_count', 'last_updated_at')
    list_filter = ('last_updated_at',)
    search_fields = ('job__title',)
