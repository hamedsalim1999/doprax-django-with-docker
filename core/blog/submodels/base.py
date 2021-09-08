from django.db import models

# base models for all models need crate and updated date
class Timestamp(models.Model):
    create = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True) 
    class Meta:
        abstract = True
# publish models about draft and publish choses with admin or user 
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
# save ip addres client for count view 
class IpAdress (Timestamp):
    ip_address = models.GenericIPAddressField()
    def __str__(self):
        return self.ip_address

