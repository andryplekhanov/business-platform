from django import template

register = template.Library()


@register.filter()
def count_percents(value, arg):
    if arg == 0:
        return 0
    return int(value * 100 / arg)
