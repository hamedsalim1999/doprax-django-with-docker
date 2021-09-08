from .base import Timestamp
from django.db import models
class Coupon(Timestamp):
    code = models.CharField(max_length=15)
    amount = models.FloatField()
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.code
