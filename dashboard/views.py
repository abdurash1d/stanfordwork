from rest_framework import generics, viewsets
from .models import JobViewLog, UserActivityLog, JobApplicationStats, AdminDashboardSettings
from .serializers import (
    JobViewLogSerializer,
    UserActivityLogSerializer,
    JobApplicationStatsSerializer,
    AdminDashboardSettingsSerializer
)
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

# Job View Log Views
class JobViewLogListView(generics.ListAPIView):
    queryset = JobViewLog.objects.all()
    serializer_class = JobViewLogSerializer
    permission_classes = [IsAdminUser]

class JobViewLogDetailView(generics.RetrieveAPIView):
    queryset = JobViewLog.objects.all()
    serializer_class = JobViewLogSerializer
    permission_classes = [IsAdminUser]

# User Activity Log Views
class UserActivityLogListView(generics.ListAPIView):
    queryset = UserActivityLog.objects.all()
    serializer_class = UserActivityLogSerializer
    permission_classes = [IsAdminUser]

class UserActivityLogDetailView(generics.RetrieveAPIView):
    queryset = UserActivityLog.objects.all()
    serializer_class = UserActivityLogSerializer
    permission_classes = [IsAdminUser]

# Job Application Stats Views
class JobApplicationStatsListView(generics.ListAPIView):
    queryset = JobApplicationStats.objects.all()
    serializer_class = JobApplicationStatsSerializer
    permission_classes = [IsAdminUser]

class JobApplicationStatsDetailView(generics.RetrieveAPIView):
    queryset = JobApplicationStats.objects.all()
    serializer_class = JobApplicationStatsSerializer
    permission_classes = [IsAdminUser]

# Admin Dashboard Settings Views
class AdminDashboardSettingsListView(generics.ListAPIView):
    queryset = AdminDashboardSettings.objects.all()
    serializer_class = AdminDashboardSettingsSerializer
    permission_classes = [IsAdminUser]

class AdminDashboardSettingsDetailView(generics.RetrieveUpdateAPIView):
    queryset = AdminDashboardSettings.objects.all()
    serializer_class = AdminDashboardSettingsSerializer
    permission_classes = [IsAdminUser]

