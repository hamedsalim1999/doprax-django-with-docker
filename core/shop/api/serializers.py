from rest_framework import serializers,viewsets
from ..models import Product,Category,Coupon,Order,OrderItem
class Productserializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields =  ('title','description','price','category','image','height_field','width_field','stock','available')
class Categoryserializers(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Category
        fields =  ('title',)

class Couponserializers(serializers.ModelSerializer):
    
    class Meta:
        model = Coupon
        fields =  ('code',)
class Orderserializers(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields =  ('items','ordered','shipping_address','coupon','being_delivered','received','refund_requested','refund_granted')
class OrderItemserializers(serializers.ModelSerializer):
    
    class Meta:
        model = OrderItem
        fields =  ('user','ordered','product','quantity')