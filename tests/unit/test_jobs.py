import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from django.contrib.auth import get_user_model
from apps.jobs.models import Job, JobCategory

User = get_user_model()

@pytest.mark.django_db
class TestJobAPI(APITestCase):
    @pytest.fixture(autouse=True)
    def setup(self, employer_user):
        self.client = APIClient()
        self.user = employer_user
        # Ensure user is active and has a usable password
        self.user.is_active = True
        self.user.set_password('testpass123')
        self.user.save()
        # Authenticate the user
        self.client.force_authenticate(user=self.user)
        # Verify authentication
        assert self.client.session._session is not None
        
        # Create a job category
        self.category = JobCategory.objects.create(
            name='Test Category',
            description='Test Category Description'
        )
        
        # Create a job with all required fields
        self.job = Job.objects.create(
            title='Test Job',
            description='Test Description',
            location='Remote',
            job_type='full-time',
            employer=self.user,
            category=self.category,
            timely_type='morning',
            gender_requirement='Any',
        )

    def test_get_job_list(self):
        url = reverse('job-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check that our test job is in the response
        job_titles = [job['title'] for job in response.data]
        self.assertIn('Test Job', job_titles)

    def test_get_job_detail(self):
        url = reverse('job-detail', args=[self.job.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Job')

    def test_create_job_authenticated(self):
        url = reverse('job-list')
        data = {
            'title': 'New Job',
            'description': 'New Job Description',
            'location': 'Remote',
            'job_type': 'full-time',
            'employer': self.user.id,
            'category': self.category.id,
            'timely_type': 'morning',
            'gender_requirement': 'Any',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Job.objects.count(), 2)
        self.assertEqual(Job.objects.latest('id').title, 'New Job')

    def test_update_job(self):
        url = reverse('job-detail', args=[self.job.id])
        data = {'title': 'Updated Job Title'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.job.refresh_from_db()
        self.assertEqual(self.job.title, 'Updated Job Title')

    def test_delete_job(self):
        job_id = self.job.id
        url = reverse('job-detail', args=[job_id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Job.objects.filter(id=job_id).exists())
