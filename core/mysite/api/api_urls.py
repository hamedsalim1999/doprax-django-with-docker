
from django.urls import path,include
from .api_views import ContactAPI_List
from rest_framework import routers
router = routers.DefaultRouter()

router.register('contact',ContactAPI_List)

urlpatterns = [
    path('v1/',include(router.urls)),
]

