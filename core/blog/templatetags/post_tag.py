from django import template
from ..models import Post,Tag

register = template.Library()

@register.inclusion_tag("share/last_post_cat.html")
def last_post():
    return{
        "last_post": Post.objects.last_post()
    }
@register.inclusion_tag("share/recent_post_cat.html")
def recent_post():
    return{
        "recent_post": Post.objects.last_post()
    }
@register.inclusion_tag("share/tag_clouds_cat.html")
def tag_clouds():
    return{
        "tag_clouds": Tag.objects.all()
    }
@register.inclusion_tag("share/search_tag.html")
def search():
    pass
    
