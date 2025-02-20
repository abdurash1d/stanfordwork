from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from .views import (JobViewSet, 
                    ApplicationViewSet, 
                    FileUploadView,
                    JobCategoryViewSet,
                    ReviewViewSet,
                    JobInquiryViewSet)


router = DefaultRouter()
router.register(r'jobs', JobViewSet)
router.register(r'applications', ApplicationViewSet)
router.register(r'jobcategories', JobCategoryViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'inquiries', JobInquiryViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path("jobs/<int:job_id>/upload/", FileUploadView.as_view(), name="file-upload"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    