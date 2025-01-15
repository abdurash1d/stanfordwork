from rest_framework import serializers
from .models import JobViewLog, UserActivityLog, JobApplicationStats, AdminDashboardSettings, JobPostingAnalytics
from jobs.models import Job
from django.contrib.auth.models import User

class JobViewLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobViewLog
        fields = '__all__'

class UserActivityLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserActivityLog
        fields = '__all__'

class JobApplicationStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplicationStats
        fields = '__all__'

class AdminDashboardSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminDashboardSettings
        fields = ['key', 'value']

class JobPostingAnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPostingAnalytics
        fields = '__all__'
