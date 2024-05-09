from django import template
from num2words import num2words

register = template.Library()

@register.filter
def amount_to_words(amount):
    try:
        # Convert amount to words using num2words library
        return num2words(amount)
    except ValueError:
        return ''
