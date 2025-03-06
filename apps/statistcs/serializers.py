from rest_framework import serializers

from apps.statistcs.models import JobPostingAnalytics
from apps.jobs.models import Job


class JobPostingAnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPostingAnalytics
        fields = '__all__'
