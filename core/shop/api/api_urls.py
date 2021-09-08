
from django.urls import path,include
from .api_views import ProductAPI_List,CategoryAPI_List,CouponAPI_List,OrderItemAPI_List,OrderAPI_List
from rest_framework import routers
router = routers.DefaultRouter()
router.register('product',ProductAPI_List)
router.register('category',CategoryAPI_List)
router.register('order',OrderItemAPI_List)
router.register('orderitem',OrderAPI_List)
router.register('coupon',CouponAPI_List)

urlpatterns = [
    path('v1/',include(router.urls)),
    
]

