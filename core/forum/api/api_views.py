from rest_framework import generics, viewsets
from rest_framework.response import Response
from .serializers import Threadserializers,Replyializers,Userserializers
from ..models import Reply,Thread
from django.contrib.auth.models import User
from ..submodels.base import IpAdress

class ReplyAPI_List(viewsets.ModelViewSet):
    queryset = Reply.objects.all()
    serializer_class = Replyializers
class ThreadAPI_List(viewsets.ModelViewSet):
    queryset = Thread.objects.all()
    serializer_class = Threadserializers

class UserApi_List(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = Userserializers


