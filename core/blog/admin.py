from django.contrib import admin
from .models import Post,Category,Tag,Comment
# Register your models here.

@admin.register(Post)
class Post_admin(admin.ModelAdmin):
    # date_hierarchy = 'create'
    # actions_on_top = False
    # actions_on_bottom = False
    # actions_selection_counter = False
    list_filter = ('category', 'create')
    filter_horizontal = ('authors','tag')
    list_display = ('title','category','tag_to_str')
    search_fields = ['title','main_text']
    fieldsets = (
        (None, {
            'fields': (('title', 'publish_status'), 'main_text', 'category',('authors'),('tag'),('hits'))
        }),
        ('upload files', {
            'fields': (('image','height_field','width_field'),('file'),('video',)),
     
        }),
    )
    def tag_to_str(self,obj):
        return ','.join([tag.title for tag in obj.tag.all()])
@admin.register(Category)
class Category_admin(admin.ModelAdmin):
    fieldsets = (
        ('Category', {
            'fields': (('title', ))
        }),
      )


@admin.register(Tag)
class Tag_admin(admin.ModelAdmin):
        fieldsets = (
        ('Tag', {
            'fields': (('title', ))
        }),
      )
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)