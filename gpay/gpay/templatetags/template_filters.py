from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='add_class')
def add_class(value, arg):
    """
    Add a CSS class to a form field, form control, or an HTML element.
    Usage: {% value|add_class:"class_name" %}
    """
    if hasattr(value, 'field'):
        # It's a form field
        css_classes = value.field.widget.attrs.get('class', '')
        if css_classes:
            css_classes = f"{css_classes} {arg}"
        else:
            css_classes = arg
        return value.as_widget(attrs={'class': css_classes})
    elif hasattr(value, '__html__'):
        # It's an HTML element
        css_classes = value.__html__().split(' ')
        if arg not in css_classes:
            css_classes.append(arg)
        return mark_safe(' '.join(css_classes))
    else:
        # It's a string
        return mark_safe(f'<span class="{arg}">{value}</span>')