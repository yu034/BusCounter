from django import template
register = template.Library()

@register.inclusion_tag('templatetags/test_tag.html')
def test_tag():
    var_example = 12312
    return {'var_example':var_example}


@register.inclusion_tag('templatetags/about.html')
def about():
    return{}

@register.inclusion_tag('templatetags/products.html')
def products():
    return{}

@register.inclusion_tag('templatetags/menu.html')
def menu():
    return{}