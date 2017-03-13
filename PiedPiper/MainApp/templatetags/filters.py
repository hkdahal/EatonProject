# Django imports
from django import template

register = template.Library()


@register.filter
def image_300(image_url):
    url_array = image_url.split('/')
    url_array[-1] = url_array[-1].replace('1', '3')
    return '/'.join(url_array)


