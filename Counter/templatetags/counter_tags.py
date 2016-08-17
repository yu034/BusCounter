from django import template
register = template.Library()

register.inclusion_tag('templatetags/test_tag.html')

def test_tag():
    var_example = 12312
    return {'var_example':var_example}