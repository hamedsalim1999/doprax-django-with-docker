from django.db import models
from .base import Timestamp
import secrets
from django.urls import reverse
from django.utils.text import slugify
class Thread(Timestamp):
    sku = models.CharField(max_length=128,primary_key= True,unique=True)
    slug = models.SlugField(max_length=128,db_index=True,unique=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    date_created = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):  
        if not self.slug :
            self.slug = slugify(f'{self.title}{secrets.token_urlsafe(4)}', allow_unicode=True)
            self.sku = secrets.token_urlsafe(16)
        super(Thread,self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('forum:detail_post', kwargs={'slug': self.slug}) 
    class Meta:
        ordering = ['-create']