from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.company.views import (CompanyViewSet, 
                    CompanyResponsiblePersonViewSet)


router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'responsible-persons', CompanyResponsiblePersonViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
