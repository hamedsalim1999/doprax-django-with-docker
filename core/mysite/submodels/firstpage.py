from django.db import models
from django.core.files import File 
import secrets
import os
from django.urls import reverse,reverse_lazy
from django.conf import settings
from .base import Publish,Timestamp
from django.utils.text import slugify
from ckeditor.fields import RichTextField
# Create your models here.
class Info(Publish):
    name = models.CharField(max_length=256)
    email = models.EmailField(max_length=254)
    description =models.CharField(max_length=500)
    logo = models.ImageField(upload_to="./info", height_field=80, width_field=80, max_length=256)
    workshop_address = models.TextField()
    office_address = models.TextField()
    detail = RichTextField()
    phonenumber = models.CharField(max_length=50, blank=True, null=True)
    faxnumber = models.CharField(max_length=50, blank=True, null=True)
    sku = models.CharField(max_length=128,primary_key= True, default = secrets.token_urlsafe(16),editable = False,unique=True)
    slug = models.SlugField(max_length=128,db_index=True,unique=True)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('blog:detail_post', kwargs={'slug': self.slug}) 
    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.title}{secrets.token_urlsafe(4)}', allow_unicode=True)
        self.sku = secrets.token_urlsafe(16)
        super(Info,self).save(*args, **kwargs)
