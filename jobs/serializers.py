from rest_framework import serializers
from .models import Job, Application
from django.contrib.auth import get_user_model

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
