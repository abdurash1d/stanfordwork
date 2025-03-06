from django.urls import path, include
from rest_framework.routers import DefaultRouter


from apps.locations.views import LocationViewSet

router = DefaultRouter()
router.register(r'locations', LocationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
]
