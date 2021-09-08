from django.db import models
from django.db.models.deletion import CASCADE
from .base import Publish
from django.utils.text import slugify
from django.urls import reverse
import secrets
from .image import Image
class Product(Publish):
    sku = models.CharField(max_length=128,primary_key= True,unique=True)
    slug = models.SlugField(max_length=128,db_index=True,unique=True)
    image = models.ForeignKey(Image,on_delete=CASCADE)
    orderitem =  models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):  
        if not self.slug :
            self.slug = slugify(f'{self.title}{secrets.token_urlsafe(4)}', allow_unicode=True)
            self.sku = secrets.token_urlsafe(16)
        super(Product,self).save(*args, **kwargs)
    
    class Meta:
        ordering = ['-orderitem']

    