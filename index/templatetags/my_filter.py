from django import template

register = template.Library()


@register.filter
def mul(v1, v2):
    try:
        return str(v1 * v2)
    except:
        return "wrong"
