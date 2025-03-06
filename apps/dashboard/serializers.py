from rest_framework import serializers
from django.contrib.auth.models import User

from apps.dashboard.models import (JobViewLog, 
                     UserActivityLog, 
                     JobApplicationStats, 
                     AdminDashboardSettings,
                     SMSNotification)
from apps.jobs.models import Job


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

class SMSNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SMSNotification
        fields = '__all__'
        