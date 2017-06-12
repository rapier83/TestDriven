from django.core.urlresolvers import resolve
from django.test import TestCase
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
