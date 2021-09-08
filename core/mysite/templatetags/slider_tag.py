from django import template
from ..models import Slider

register = template.Library()

@register.inclusion_tag("share/slider_cat.html")
def slider():
    return{
        "slider": Slider.objects.all()
    }
    