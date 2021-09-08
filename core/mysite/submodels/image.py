from django.db import models
from django.core.files import File 
import secrets
import os
from django.urls import reverse,reverse_lazy
from django.conf import settings
from .base import Publish,Timestamp
from django.utils.text import slugify

class Image(Timestamp):
    title = models.CharField(max_length=128, null=True)
    sku = models.CharField(max_length=128,primary_key= True, default = secrets.token_urlsafe(16),editable = False,unique=True)
    slug = models.SlugField(max_length=128,db_index=True,unique=True)
    description = models.CharField(max_length=512,blank=True, null=True)
    image = models.ImageField(max_length=128,upload_to='./info', height_field='height_field', width_field='width_field')
    height_field = models.PositiveIntegerField(default='480',blank=True, null=True)
    width_field  = models.PositiveIntegerField(default='720',blank=True, null=True)
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.title}{secrets.token_urlsafe(4)}', allow_unicode=True)
        self.sku = secrets.token_urlsafe(16)
        super(Image,self).save(*args, **kwargs)

