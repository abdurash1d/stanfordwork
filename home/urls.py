from django.urls import path
from . import views
from .views import test_email

urlpatterns = [
    path('', views.index, name='home.index'),
    path('about', views.about, name='home.about'),
    path('test-email/', test_email, name='test_email'),
    
]