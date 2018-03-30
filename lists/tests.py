from django.test import TestCase

class SmokeCheck(TestCase):

    def test_physics(self):
        self.assertEqual(1+1, 3)
