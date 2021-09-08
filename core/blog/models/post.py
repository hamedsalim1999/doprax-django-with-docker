from django.db import models
import secrets
from django.urls import reverse
from django.utils.text import slugify
from django.conf import settings
from .base import Publish,IpAdress
from .category import Category
from .tag import Tag
from ckeditor.fields import RichTextField



# my queryset
class PostQuerySet(models.QuerySet):
    def last_post(self):
        return self.order_by('-create')[:6]
# my manager
class PostManager(models.Manager):
    def get_queryset(self) :
        return PostQuerySet(self.model,using=self.db)
    def published(self):
        return self.filter(publish_status = 'P')
    def summery(self):
        return self.main_text[:150]

    def most_post(self):
        this_month_post = self.dates('-create', 'month')
        return this_month_post.hits[5]
    def last_post(self):
        return self.get_queryset().last_post()
# my models
class Post (Publish):
    title = models.CharField(max_length=128, null=True)
    sku = models.CharField(max_length=128,primary_key= True,unique=True)
    slug = models.SlugField(max_length=128,db_index=True,unique=True)
    main_text = RichTextField()
    image = models.ImageField(max_length=128,upload_to='blog/post/image', height_field='height_field', width_field='width_field',blank=True, null=True)
    height_field = models.PositiveIntegerField(default='480',blank=True, null=True)
    width_field  = models.PositiveIntegerField(default='720',blank=True, null=True)
    video = models.URLField(max_length=512 , blank=True, null=True)
    file = models.FileField(upload_to='blog/post/file',blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default= 'no category' , null =True)
    authors = models.ManyToManyField(settings.AUTH_USER_MODEL)
    tag = models.ManyToManyField(Tag)
    summary = models.CharField(max_length=500)
    hits = models.ManyToManyField(IpAdress,blank=True, null=True , related_name="hits")
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog:detail_post', kwargs={'slug': self.slug}) 

    def save(self, *args, **kwargs):  
        if self.main_text:
            self.summary = self.main_text[:500]
        if not self.slug :
            self.slug = slugify(f'{self.title}{secrets.token_urlsafe(4)}', allow_unicode=True)
            self.sku = secrets.token_urlsafe(16)
        super(Post,self).save(*args, **kwargs)
    class Meta:
        ordering = ['-create']
    objects = PostManager()

