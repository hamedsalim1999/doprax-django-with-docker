from django.db import models
import secrets
from .base import Timestamp
from django.utils.text import slugify
class Tag(Timestamp):
    sku = models.CharField(max_length=128,primary_key= True, default = secrets.token_urlsafe(16),editable = False)
    title = models.CharField(max_length=128, null=True)
    slug = models.SlugField(max_length=128,db_index=True,unique=True)
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        
        self.sku = f'tag_{secrets.token_urlsafe(8)}'

        self.slug = slugify(self.title, allow_unicode=True)

        super(Tag, self).save(*args, **kwargs)