from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

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
    
# class Rating(Publish):
#     score = models.IntegerField(default=0,
#         validators=[
#             MaxValueValidator(5),
#             MinValueValidator(0),
#         ]
#     )
#     user =models.ForeignKey(User, related_name='USER', on_delete=models.CASCADE)
#     def __str__(self):
#         return str(self.pk)

#     class Meta:
#         abstract = True
class IpAdress (Timestamp):
    ip_address = models.GenericIPAddressField()
    def __str__(self):
        return self.ip_address