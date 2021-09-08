from rest_framework import viewsets
from .serializers import Categoryserializers,Postserializers,Userserializers,Tagializers,Ipsializers,Commentsializers
from .models.post import Post
from .models.category import Category
from .models.tag import Tag
from .models.comments import Comment
from django.contrib.auth.models import User
from ..submodels.base import IpAdress


class PostAPI_List(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = Postserializers
class IpAPI_List(viewsets.ModelViewSet):
    queryset = IpAdress.objects.all()
    serializer_class = Ipsializers
class CategoryAPI_List(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = Categoryserializers
class TagAPI_List(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = Tagializers
class UserApi_List(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = Userserializers
class CommentApi_List(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = Commentsializers


