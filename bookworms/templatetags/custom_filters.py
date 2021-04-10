from django import template

register=template.Library()


def range_filter(value):
    if len(value)>200:
        return value[0:200]+"........"+len(value)

    else:
        return value[:]+""

register.filter('range_filter',range_filter)
