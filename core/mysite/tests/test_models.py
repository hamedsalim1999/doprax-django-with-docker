from django.test import TestCase
from django.utils import timezone
from ..models import Image
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
class ImageModels(TestCase):
   
    def setUp(self):
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

    def test_image101(self):
        image101 = Image(
            sku = 'bVaqNzzFScfY219Bh_XikQ',
            title ='test101 image title',
            description ='this is description for exaple ' ,
            image = "this_is_test_image.png",
      
        )  

        # test_image101.authors.add(self.user101)
        # test_image101.authors.add(self.user102)
        image101.save()
        self.assertEquals(str(image101.image),'this_is_test_image.png')

