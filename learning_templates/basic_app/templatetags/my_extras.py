from atexit import register
from django import template
register = template.Library()

def cut(value,arg):

    return value.replace(arg,'') # This will look for the arg in our original string and replace it with the second parameter

register.filter('cut',cut)