from django.db import models
import secrets
from .base import Timestamp
from django.utils.text import slugify
class Category(Timestamp):
    sku = models.CharField(max_length=128,primary_key= True, default = secrets.token_urlsafe(16),editable = False)
    title = models.CharField(max_length=128, null=True)
    slug = models.SlugField(max_length=128,db_index=True,unique=True)
    def __str__(self):
        return self.title
    # save sku(id for record) and slug( for url )
    def save(self, *args, **kwargs):  
        if not self.slug :
            self.slug = slugify(f'{self.title}{secrets.token_urlsafe(4)}', allow_unicode=True)
            self.sku = secrets.token_urlsafe(16)
        super(Category,self).save(*args, **kwargs)


