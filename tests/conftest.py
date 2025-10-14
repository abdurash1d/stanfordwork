import os
import pytest
from django.test import Client, TestCase, override_settings
from django.contrib.auth import get_user_model
from django.db import transaction
from django.urls import reverse
from django.core.management import call_command
from rest_framework.test import APIClient

User = get_user_model()

@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    """Ensure test database is created and migrations are applied."""
    with django_db_blocker.unblock():
        # Apply migrations
        call_command('migrate', '--noinput')
        # Create a superuser for admin tests if it doesn't exist
        if not User.objects.filter(username='admin').exists():
            with transaction.atomic():
                User.objects.create_superuser(
                    email='admin@example.com',
                    username='admin',
                    password='testpass123',
                    first_name='Admin',
                    last_name='User',
                    role='admin'
                )

@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    """Give all tests access to the database.
    
    This fixture is automatically used for all tests.
    """
    pass

@pytest.fixture
def client():
    """Django test client."""
    return Client()

@pytest.fixture
def api_client():
    """API test client."""
    return APIClient()

@pytest.fixture
def admin_user(db):
    """Create an admin user for testing."""
    with transaction.atomic():
        user, created = User.objects.get_or_create(
            username='testadmin',
            defaults={
                'email': 'testadmin@example.com',
                'password': 'testpass123',
                'first_name': 'Test',
                'last_name': 'Admin',
                'role': 'admin',
                'is_staff': True,
                'is_superuser': True
            }
        )
    return user

@pytest.fixture
def regular_user(db):
    """Create a regular user for testing."""
    with transaction.atomic():
        user, created = User.objects.get_or_create(
            username='testuser',
            defaults={
                'email': 'testuser@example.com',
                'first_name': 'Test',
                'last_name': 'User',
                'role': 'candidate',
                'is_active': True
            }
        )
        if created or not user.check_password('testpass123'):
            user.set_password('testpass123')
            user.save()
    return user

@pytest.fixture
def employer_user(db):
    """Create an employer user for testing."""
    with transaction.atomic():
        user, created = User.objects.get_or_create(
            username='testemployer',
            defaults={
                'email': 'employer@example.com',
                'first_name': 'Test',
                'last_name': 'Employer',
                'role': 'employer',
                'is_active': True
            }
        )
        if created or not user.check_password('testpass123'):
            user.set_password('testpass123')
            user.save()
    return user
