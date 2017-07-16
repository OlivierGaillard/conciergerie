from django.test import TestCase
from conciergerie.forms import TravailFilterForm
# Create your tests here.
class TestValidation(TestCase):

    def test_month_zero(self):
        form = TravailFilterForm({'month' : 1})
        self.assertFalse(form.is_valid())




