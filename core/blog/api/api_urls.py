from django.urls import path,include
from .api_views import CategoryAPI_List,PostAPI_List,TagAPI_List,UserApi_List,IpAPI_List,CommentApi_List
from rest_framework import routers
router = routers.DefaultRouter()
router.register('post',PostAPI_List)
router.register('category',CategoryAPI_List)
router.register('tag',TagAPI_List)
router.register('users',UserApi_List)
router.register('Ip',IpAPI_List)
router.register('comment',CommentApi_List)
urlpatterns = [
    path('v1/',include(router.urls)),
    
]

