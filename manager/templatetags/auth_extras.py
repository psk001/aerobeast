from django import template
from django.contrib.auth.models import Group 

register = template.Library()

@register.filter(name='has_group')
def has_group(user, group_name): 
    group = Group.objects.get(name='ATC-Group') 
    return True if group in user.groups.all() else False

# @register.filter
# def get_type(value):
#     return type(value)