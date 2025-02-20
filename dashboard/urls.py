from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .views import SMSNotificationViewSet

router = DefaultRouter()
router.register(r'notifications', SMSNotificationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('job-view-logs/', views.JobViewLogListView.as_view(), name='job-view-logs-list'),
    path('job-view-logs/<int:pk>/', views.JobViewLogDetailView.as_view(), name='job-view-log-detail'),
    path('user-activity-logs/', views.UserActivityLogListView.as_view(), name='user-activity-logs-list'),
    path('user-activity-logs/<int:pk>/', views.UserActivityLogDetailView.as_view(), name='user-activity-log-detail'),
    path('job-application-stats/', views.JobApplicationStatsListView.as_view(), name='job-application-stats-list'),
    path('job-application-stats/<int:pk>/', views.JobApplicationStatsDetailView.as_view(), name='job-application-stats-detail'),
    path('admin-dashboard-settings/', views.AdminDashboardSettingsListView.as_view(), name='admin-dashboard-settings-list'),
    path('admin-dashboard-settings/<int:pk>/', views.AdminDashboardSettingsDetailView.as_view(), name='admin-dashboard-settings-detail'),
    
]
