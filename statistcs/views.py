from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import JobPostingAnalytics
from .serializers import (
    JobPostingAnalyticsSerializer
)
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response


class JobPostingAnalyticsListView(generics.ListAPIView):
    queryset = JobPostingAnalytics.objects.all()
    serializer_class = JobPostingAnalyticsSerializer
    permission_classes = [IsAdminUser]

class JobPostingAnalyticsDetailView(generics.RetrieveAPIView):
    queryset = JobPostingAnalytics.objects.all()
    serializer_class = JobPostingAnalyticsSerializer
    permission_classes = [IsAdminUser]