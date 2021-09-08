from django.test import TestCase,SimpleTestCase
from blog.views import post_view,success,post_detail
from django.urls import resolve,reverse


class TestUrls(TestCase):
    def test_index_url(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func.view_class ,post_view)

    def test_success_url(self):
        url = reverse('success')
        self.assertEquals(resolve(url).func.view_class ,success)
    def test_detail_url(self):
        url = reverse('detail',args=['0x-ruyvahjVRNUE7Bv7_FQ'])
        # url = "/0x-ruyvahjVRNUE7Bv7_FQ/"
        self.assertEquals(resolve(url).func.view_class ,post_detail)