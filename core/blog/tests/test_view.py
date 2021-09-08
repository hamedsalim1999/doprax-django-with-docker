from django.test import TestCase,Client
from django.urls import resolve
from ..models import Post,Category 
import json
class PostTest(TestCase):
    def set_up(self):
        cliendt = cliendt()
        self.list_url = resolve('list')
        self.detail_url = resolve('deail',args=['esX0TUdixfL6V8KZbmrKMQ'])
        Post.objects.create(
            sku = 'esX0TUdixfL6V8KZbmrKMQ',
            title = 'test title ',
            slug = 'testtitle_slug',
            main_text = 'test it is test text for 999999 this is tsest 9999 ',
            scoring = '5',
            category ='python',
            authors = 'user 1 ',)
    def post_test(self):
        response =self.client.get(self.list_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response , 'post.html')
