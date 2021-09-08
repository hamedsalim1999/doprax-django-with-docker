from django.contrib import admin
from .models import Product,Category,Coupon,OrderItem,Order,Address

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # date_hierarchy = 'create'
    # actions_on_top = False
    # actions_on_bottom = False
    # actions_selection_counter = False
    list_filter = ('category', 'create')
    list_display = ('title','category')
    search_fields = ['title','main_text']
    fieldsets = (
        (None, {
            'fields': (('title', 'available'), 'description', 'category',('stock') ,('price'))
        }),
        ('upload files', {
            'fields': (('image','height_field','width_field'),),
     
        }),
    )
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Category', {
            'fields': (('title', ))
        }),
      )
@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    pass
@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    pass