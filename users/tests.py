from django.test import TestCase
from django.contrib.auth.models import Group, Permission
from django.urls import reverse

from .models import User, Resume


class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='password123',
            role='candidate'
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'testuser@example.com')
        self.assertTrue(self.user.check_password('password123'))
        self.assertEqual(self.user.role, 'candidate')

    def test_str_representation(self):
        self.assertEqual(str(self.user), "testuser (candidate)")


class ResumeModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.resume = Resume.objects.create(user=self.user, file='test_resume.pdf')

    def test_resume_creation(self):
        self.assertEqual(self.resume.user.username, 'testuser')
        self.assertEqual(self.resume.file, 'test_resume.pdf')


class GroupTest(TestCase):
    def setUp(self):
        self.group = Group.objects.create(name='Test Group')

    def test_group_creation(self):
        self.assertEqual(self.group.name, 'Test Group')


class PermissionTest(TestCase):
    def setUp(self):
        self.permission = Permission.objects.create(
            name='Can View Dashboard',
            codename='can_view_dashboard',
            content_type_id=1  
        )

    def test_permission_creation(self):
        self.assertEqual(self.permission.name, 'Can View Dashboard')


class UserViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='password123',
            role='candidate'
        )

    def test_user_list_view(self):
        response = self.client.get(reverse('user-list'))
        self.assertEqual(response.status_code, 200)

    def test_user_detail_view(self):
        response = self.client.get(reverse('user-detail', kwargs={'pk': self.user.pk}))
        self.assertEqual(response.status_code, 200)
