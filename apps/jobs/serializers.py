from rest_framework import serializers
from django.contrib.auth import get_user_model

from apps.jobs.models import (Job, 
                     Application,
                     JobCategory,
                     JobInquiry,
                     Review)


class JobSerializer(serializers.ModelSerializer):
    employer = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all())

    class Meta:
        model = Job
        fields = '__all__'


class ApplicationSerializer(serializers.ModelSerializer):
    job = JobSerializer(read_only=True)
    candidate = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all())
    
    class Meta:
        model = Application
        fields = '__all__'


class JobCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobCategory
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class JobInquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobInquiry
        fields = '__all__'
