from django import template
from entrys.models import Entry

register = template.Library()

@register.filter
def keyvalue(dict, key):
    try:
        return dict[key]
    except KeyError:
        return ''