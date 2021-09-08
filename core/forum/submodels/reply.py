from django.db import models
from django.contrib.auth.models import User 
from .thread import Thread
from .base import Timestamp
class Reply(Timestamp):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    def __str__(self):
        return self.thread.title