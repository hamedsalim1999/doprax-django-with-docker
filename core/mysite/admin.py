from django.contrib import admin
from .models import Contact,Image,Info,Slider
# Register your models here.
@admin.register(Contact)
class Contact_admin(admin.ModelAdmin):
    pass
@admin.register(Image)
class Image_admin(admin.ModelAdmin):
    fieldsets = (
        ('Image', {
            'fields': (('title','image' ))
        }),('More info' , {
            'fields':(('description','height_field','width_field'))
        })
      )
@admin.register(Info)
class Info_admin(admin.ModelAdmin):
    pass
@admin.register(Slider)
class Slider_admin(admin.ModelAdmin):
    fieldsets = (
            ('Image', {
            'fields': (('publish_status','image','orderitem' ))
        }),
    )