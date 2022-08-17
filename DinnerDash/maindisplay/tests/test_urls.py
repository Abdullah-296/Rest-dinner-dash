from django.test import TestCase


class TestLink(TestCase):
    def test_home_page(self):
        response = self.client.get('874981798')
        self.assertEqual(response.status_code, 404)
