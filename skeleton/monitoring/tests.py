from django.test import TestCase, Client
from django.urls import reverse


class MonitoringViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_request_to_ping_url_resolver_returns_http_200_response(self):
        ping_url = reverse('ping')
        response = self.client.get(ping_url)

        assert response.status_code == 200

    def test_request_to_ping_url_resolver_returns_content_bytes_ok(self):
        ping_url = reverse('ping')
        response = self.client.get(ping_url)

        assert response.content == b'OK'
