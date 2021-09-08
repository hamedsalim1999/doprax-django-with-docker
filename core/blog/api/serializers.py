from rest_framework import serializers
from ..models import Post,Category,Tag,Comment
from .models.base import IpAdress
from django.contrib.auth.models import User
class Postserializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields =  '__all__'
class Categoryserializers(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Category
        fields =  ('title',)

class Userserializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields =  '__all__'
class Tagializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('title',)
class Ipsializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IpAdress
        fields =  '__all__'
class Commentsializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields =  '__all__'

