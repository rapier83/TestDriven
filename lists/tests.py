from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import HomePage


# Create your tests here.

# class SmokeTest(TestCase):
#
#     def TestBadMath(self):
#         self.assertEqual(1 + 1, 3)


class HomePageTest(TestCase):

    def testRootURLResolve(self):
        found = resolve('/')
        self.assertEqual(found.func, HomePage)

    def testReturnCorrectHtml(self):
        request = HttpRequest()
        response = HomePage(request)
        # self.assertTrue(response.content.startswith(b'<html>'))
        # self.assertIn(b'<title>To-Do Lists</title>', response.content)
        # self.assertTrue(response.content.strip().endswith(b'</html>'))
        expected = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected)

    def TestPostRequest(self):
        request = HttpRequest()
        request.method = "POST"
