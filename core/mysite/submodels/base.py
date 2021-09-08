from django.db import models
from django.utils import timezone

class Timestamp(models.Model):
    create = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True) 
    class Meta:
        abstract = True
class Publish(Timestamp):
    DRAFT = 'D'
    PUBLISH = 'P'
    STATUS = (
        (DRAFT , 'DRAFT'),
        (PUBLISH,'PUBLISH'),
        )
    publish_status = models.CharField( max_length=1,
        choices=STATUS,
        default=PUBLISH)
    class Meta:
        abstract = True
