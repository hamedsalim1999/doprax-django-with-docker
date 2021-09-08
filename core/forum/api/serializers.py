from rest_framework import serializers
from ..models import Reply,Thread
from ..submodels.base import IpAdress
from django.contrib.auth.models import User


class Threadserializers(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields =  '__all__'

class Replyializers(serializers.ModelSerializer):
    thread = serializers.PrimaryKeyRelatedField(queryset=Thread.objects.all(),allow_null=True)
    class Meta:
        model = Reply
        fields =  '__all__'

class Userserializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =  '__all__'



