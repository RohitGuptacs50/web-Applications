from django.test import TestCase , Client
from .models import Add

# Create your tests here.


class SumTestCsae(TestCase):

    def setUp(self):

        # Create Add objects or dummy data
        A1 = Add.objects.create(n = 0, m = 0, res = 0)
        A2 = Add.objects.create(n = -1, m = -1, res = -2)
        A3 = Add.objects.create(n = 1.2, m = 1.8, res = 3.0)


    def TestSumValid(self):
        n = Add.objects.get(n = 0)
        m = Add.objects.get(m = 0)
        res = Add.objects.get(res = 0)
        self.assertTrue(Add.is_valid_variable())


    
    def test_input(self):             # To check response of the input page
        c = Client()
        response = c.get('')
        self.assertEqual(response.status_code, 200)