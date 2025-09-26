# in poll/templatetags/poll_extras.py
from django import template
register = template.Library()

@register.filter
def percent(part, whole):
    try:
        return 100 * part / whole
    except (ZeroDivisionError, TypeError):
        return 0
