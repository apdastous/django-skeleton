from django.test import TestCase, Client
from django.urls import reverse


class RootViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_request_to_root_url_resolver_returns_http_200_response(self):
        root_url = reverse('root')
        response = self.client.get(root_url)

        assert response.status_code == 200
