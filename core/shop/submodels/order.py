from django.db import models
import secrets
from .base import Timestamp
from django.conf import settings
from django.utils.text import slugify
from .orderItem import OrderItem
from .address import Address
from .coupon import Coupon

class Order(Timestamp):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    ordered = models.BooleanField(default=False)
    shipping_address = models.ForeignKey(Address, related_name='shipping_address', on_delete=models.SET_NULL, blank=True, null=True)
    coupon = models.ForeignKey(Coupon, on_delete=models.SET_NULL, blank=True, null=True)
    being_delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    refund_requested = models.BooleanField(default=False)
    refund_granted = models.BooleanField(default=False)
    sku = models.CharField(max_length=128,primary_key= True, default = secrets.token_urlsafe(16),editable = False)
    slug = models.SlugField(max_length=128,db_index=True,unique=True)
    '''
    1. Item added to cart
    2. Adding a billing address
    (Failed checkout)
    3. Payment
    (Preprocessing, processing, packaging etc.)
    4. Being delivered
    5. Received
    6. Refunds
    '''

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_total_discount_item_price(self):
        return self.quantity * self.item.price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_item_price()

    def get_final_price(self):
        if self.item.price:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()
    def save(self, *args, **kwargs):  

        if not self.slug :
            self.slug = slugify(secrets.token_urlsafe(16), allow_unicode=True)
            self.sku = secrets.token_urlsafe(16)
        super(Order,self).save(*args, **kwargs)

    def __str__(self):
        return self.slug
    class Meta:
        ordering = ['-create']
