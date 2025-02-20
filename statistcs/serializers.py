from rest_framework import serializers

from .models import  JobPostingAnalytics
from jobs.models import Job


class JobPostingAnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPostingAnalytics
        fields = '__all__'
