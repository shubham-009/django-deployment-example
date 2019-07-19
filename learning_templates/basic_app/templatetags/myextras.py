from django import template

register = template.library()

@register.filter(name=cut)
def cut(value,arg):
    """
    This cuts out all the value of "arg" from string!
    """

    return value.replace(arg,'')

# register.filter('cut',cut)
