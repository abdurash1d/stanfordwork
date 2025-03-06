from django.urls import path

from apps.statistcs import views

urlpatterns = [
    path('job-posting-analytics/', views.JobPostingAnalyticsListView.as_view(), name='job-posting-analytics-list'),
    path('job-posting-analytics/<int:pk>/', views.JobPostingAnalyticsDetailView.as_view(), name='job-posting-analytics-detail'),
    
]
