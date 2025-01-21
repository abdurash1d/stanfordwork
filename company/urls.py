from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, CompanyResponsiblePersonViewSet

# Create a router and register our viewsets
router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'responsible-persons', CompanyResponsiblePersonViewSet)

# The API URLs are now determined automatically by the router
urlpatterns = [
    path('', include(router.urls)),
]
