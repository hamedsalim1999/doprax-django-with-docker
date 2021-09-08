from django import template
from ..models import Category

register = template.Library()

@register.simple_tag
def title( data = 'Blog'):
    return data

@register.inclusion_tag("share/navbar_cat.html")
def category_navbar():
    return{
        "category": Category.objects.all()
    }
    