# Django imports
from django import template

register = template.Library()


@register.filter
def image_300(image_url):
    # http://is4.mzstatic.com/image/thumb/Music6/v4/04/41/20/04412072-8873-6ad7-267f-722c1c930946/source/100x100bb.jpg
    url_array = image_url.split('/')
    url_array[-1] = url_array[-1].replace('1', '3')
    return '/'.join(url_array)


