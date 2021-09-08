from django.db import models
from .base import Timestamp

class Contact(Timestamp):
    title = models.CharField(max_length=256)
    email = models.EmailField()
    body = models.TextField()
    name = models.CharField(max_length=256, blank=True, null=True)
    def __str__(self):
        return self.title