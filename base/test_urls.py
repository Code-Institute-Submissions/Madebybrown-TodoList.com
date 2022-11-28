from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from . import views


class TestUrls(SimpleTestCase):

    def test_login_url_is_resolved(self):
        url = reverse('login')
        print(resolve(url))
