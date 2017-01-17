from django.core.cache import cache
from django import template

from quotequota.models import Quote

register = template.Library()

@register.simple_tag
def quotecount():
    return str(cache.get_or_set('quotes_count', Quote.objects.count, timeout=300))
