"""Test views for the application."""
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class TestHomeView(TestCase):
    def test_home_view(self):
        """Test that the home page loads correctly."""
        response = self.client.get(reverse('home.index'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response, 'home/index.html')
