"""
URL configuration for standfordwork project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from jobs.views import JobViewSet
# from users.views import UserProfileViewSet

# router = DefaultRouter()
# router.register('jobs', JobViewSet, basename='job')
# router.register('users', UserProfileViewSet, basename='user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('api/jobs/', include('jobs.urls')),  # Include URLs for the jobs app (from jobs/urls.py)
    path('api/users/', include('users.urls')),  # If you have a users app, include its URLs\
    path('dashboard/', include('dashboard.urls')),  # Includes dashboard-related endpoints
    # path('api/', include(router.urls)),
    
]
