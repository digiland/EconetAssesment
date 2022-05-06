from django.test import TestCase

# Create your tests here.
from .models import Street


class TestStreet(TestCase):
    def test_str(self):
        street = Street(street_name='test')
        self.assertEqual(str(street), 'test')
