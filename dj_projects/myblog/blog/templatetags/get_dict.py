from django import template

register = template.Library()

@register.filter(name='get_filter')

def get_filter(dict, key):
    return dict.get(key)