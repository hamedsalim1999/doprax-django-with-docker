from ..submodels.product import Product
from django.db import models
import secrets
from .base import Timestamp
from django.utils.text import slugify
from django.conf import settings

class OrderItem(Timestamp):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    sku = models.CharField(max_length=128,primary_key= True, default = secrets.token_urlsafe(16),editable = False)
    slug = models.SlugField(max_length=128,db_index=True,unique=True)
    ordered = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.title}"

    def get_total_product_price(self):
        return self.quantity * self.product.price

    def get_total_discount_product_price(self):
        return self.quantity * self.product.price

    def get_amount_saved(self):
        return self.get_total_product_price() - self.get_total_discount_product_price()

    def get_final_price(self):
        if self.product.price:
            return self.get_total_discount_product_price()
        return self.get_total_product_price()
    def save(self, *args, **kwargs):  

        if not self.slug :
            self.slug = slugify(f'{self.product}{secrets.token_urlsafe(8)}', allow_unicode=True)
            self.sku = secrets.token_urlsafe(16)
        super(OrderItem,self).save(*args, **kwargs)

    class Meta:
        ordering = ['-create']


    