import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.mark.django_db
class TestUserAPI(APITestCase):
    @pytest.fixture(autouse=True)
    def setup(self, regular_user):
        self.client = APIClient()
        self.user = regular_user
        # Ensure user is active and has a usable password
        self.user.is_active = True
        self.user.set_password('testpass123')
        self.user.save()
        # Authenticate the user
        self.client.force_authenticate(user=self.user)
        # Verify authentication
        assert self.client.session._session is not None

    def test_get_user_profile(self):
        url = reverse('user-detail', args=[self.user.id])
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['email'] == self.user.email

    def test_update_user_profile(self):
        url = reverse('user-detail', args=[self.user.id])
        data = {
            'first_name': 'Updated',
            'last_name': 'Name'
        }
        response = self.client.patch(url, data, format='json')
        assert response.status_code == status.HTTP_200_OK
        self.user.refresh_from_db()
        assert self.user.first_name == 'Updated'
