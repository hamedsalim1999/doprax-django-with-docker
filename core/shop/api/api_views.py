from rest_framework import viewsets
from .serializers import Categoryserializers,Productserializers,OrderItemserializers,Orderserializers,Couponserializers
from ..models import Product,Category,Coupon,Order,OrderItem

class ProductAPI_List(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = Productserializers
class CategoryAPI_List(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = Categoryserializers
class CouponAPI_List(viewsets.ModelViewSet):
    queryset = Coupon.objects.all()
    serializer_class = Couponserializers
class OrderItemAPI_List(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemserializers
class OrderAPI_List(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = Orderserializers
