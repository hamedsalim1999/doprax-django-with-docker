from django.test import TestCase
from django.urls import reverse
from mysite.views import contact_form
from django.urls import resolve,reverse
# Create your tests here.
def test_contact_url(self):
    url = reverse('contact')
    self.assertEquals(resolve(url).func.view_class ,contact_form)
