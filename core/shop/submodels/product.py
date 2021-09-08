from django.db import models
import secrets
from django.db.models.fields import IntegerField
from django.shortcuts import reverse
from django.db.models.fields.files import ImageField
from .base import Timestamp
from .category import Category
from django.utils.text import slugify
class ProductManager(models.Manager):
    def available(self):
        return self.filter(available = True)
    

class Product(Timestamp):
    sku = models.CharField(max_length=128,primary_key= True, default = secrets.token_urlsafe(16),editable = False)
    slug = models.SlugField(max_length=128,db_index=True,unique=True)
    title = models.CharField(max_length=128, null=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10 , decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default= 'no category' , null =True)
    image = models.ImageField(max_length=128,upload_to='shop/product/image', height_field='height_field', width_field='width_field',blank=True, null=True)
    height_field = models.PositiveIntegerField(default='480',blank=True, null=True)
    width_field  = models.PositiveIntegerField(default='720',blank=True, null=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True) 
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):  

        if not self.slug :
            self.slug = slugify(f'{self.title}{secrets.token_urlsafe(4)}', allow_unicode=True)
            self.sku = secrets.token_urlsafe(16)
        super(Product,self).save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse("shop:detail", kwargs={
            'slug': self.slug
        })

    def get_add_to_cart_url(self):
        return reverse("shop:add-to-cart", kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse("shop:remove-from-cart", kwargs={
            'slug': self.slug
        })
    class Meta:
        ordering = ['-create']
    objects = ProductManager()