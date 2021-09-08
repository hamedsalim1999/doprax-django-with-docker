from django.test import TestCase
from django.utils import timezone
from ..models import Post,Category,Comment,Tag
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
class PostModels(TestCase):
   
    def setUp(self):
        self.category1 = Category.objects.create(
            title = 'test101-category',  
        )
        self.tag1 = Tag.objects.create(
            title = 'tag101',  
        )
        self.tag2 = Tag.objects.create(
            title = 'tag102',  
        )
        self.user101 = User.objects.create_user(
            username='asqar ali farhadi',
            email='testkon@mail.com',
            password='testbotnottest'
        )
        self.user102 = User.objects.create_user(
            username='asqar ali farhadi iranmaneshe tablo abadi',
            email='testkon102@mail.com',
            password='101notbe102'
        )

    def test_post101(self):
        post101 = Post(
            sku = 'bVaqNzzFScfY219Bh_XikQ',
            title ='test101 title',
            main_text ='this is main text for exaple ' ,
            scoring ='2' ,
            category = self.category1,
            slug = 'test010'
        )  
        post101.tag.add(self.tag1)
        post101.authors.add(self.user101)
        post101.authors.add(self.user102)
        post101.save()
        self.assertEquals(post101.title,'test101 title')


    def test_post102(self):
        post102 =Post(
            sku = 'bVaqNzzFScfY219Bh_XiL5',
            title ='test101 titlesss',
            main_text ='this is main text for exaple ' ,
            scoring ='22' ,
            category = self.category1,
            )
        post102.tag.add(self.tag2)
        post102.authors.add(self.user102)
        post102.save()
        self.assertEquals(post102.scoring,'22')
