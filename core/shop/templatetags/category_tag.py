from django import template
from ..models import Category

register = template.Library()

@register.inclusion_tag("share/product_category_cat.html")
def category():
    return{
        "category": Category.objects.all()
    }
    