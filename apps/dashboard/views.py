from rest_framework import generics, viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.dashboard.models import (JobViewLog, 
                     UserActivityLog, 
                     JobApplicationStats, 
                     AdminDashboardSettings,
                     SMSNotification)

from apps.dashboard.serializers import (JobViewLogSerializer, 
                          UserActivityLogSerializer,
                          JobApplicationStatsSerializer,
                          AdminDashboardSettingsSerializer,
                          SMSNotificationSerializer)


class JobViewLogListView(generics.ListAPIView):
    queryset = JobViewLog.objects.all()
    serializer_class = JobViewLogSerializer
    permission_classes = [IsAdminUser]


class JobViewLogDetailView(generics.RetrieveAPIView):
    queryset = JobViewLog.objects.all()
    serializer_class = JobViewLogSerializer
    permission_classes = [IsAdminUser]


class UserActivityLogListView(generics.ListAPIView):
    queryset = UserActivityLog.objects.all()
    serializer_class = UserActivityLogSerializer
    permission_classes = [IsAdminUser]


class UserActivityLogDetailView(generics.RetrieveAPIView):
    queryset = UserActivityLog.objects.all()
    serializer_class = UserActivityLogSerializer
    permission_classes = [IsAdminUser]


class JobApplicationStatsListView(generics.ListAPIView):
    queryset = JobApplicationStats.objects.all()
    serializer_class = JobApplicationStatsSerializer
    permission_classes = [IsAdminUser]


class JobApplicationStatsDetailView(generics.RetrieveAPIView):
    queryset = JobApplicationStats.objects.all()
    serializer_class = JobApplicationStatsSerializer
    permission_classes = [IsAdminUser]


class AdminDashboardSettingsListView(generics.ListAPIView):
    queryset = AdminDashboardSettings.objects.all()
    serializer_class = AdminDashboardSettingsSerializer
    permission_classes = [IsAdminUser]


class AdminDashboardSettingsDetailView(generics.RetrieveUpdateAPIView):
    queryset = AdminDashboardSettings.objects.all()
    serializer_class = AdminDashboardSettingsSerializer
    permission_classes = [IsAdminUser]
    

class SMSNotificationViewSet(viewsets.ModelViewSet):
    queryset = SMSNotification.objects.all()
    serializer_class = SMSNotificationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    