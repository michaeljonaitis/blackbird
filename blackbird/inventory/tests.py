from django.test import TestCase

# Create your tests here.

class BasicTest(TestCase):

    def test_test(self):
        self.assertEqual('tom', 'tom')
