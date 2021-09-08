
from django.urls import path,include
from .api_views import ReplyAPI_List , ThreadAPI_List
from rest_framework import routers
router = routers.DefaultRouter()
router.register('reply',ReplyAPI_List)
router.register('thread',ThreadAPI_List)

urlpatterns = [
    path('v1/',include(router.urls)),
    
]

