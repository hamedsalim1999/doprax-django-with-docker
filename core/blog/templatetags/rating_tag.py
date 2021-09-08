from django import template
from ..models import Post

register = template.Library()

@register.inclusion_tag("share/rating_tag.html")
def score():
    return{
        "score": Post.score
    }
    