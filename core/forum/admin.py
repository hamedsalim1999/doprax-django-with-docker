from django.contrib import admin
from .models import Thread,Reply
# Register your models here.
@admin.register(Thread)
class Thread_admin(admin.ModelAdmin):
    pass
@admin.register(Reply)
class Reply_admin(admin.ModelAdmin):
    pass