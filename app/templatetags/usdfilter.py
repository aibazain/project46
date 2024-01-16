from django import template
register=template.Library()
@register.filter('swapping')
def swap(value):
    return value.swapcase()

def remove(value,agr):
    return value.replace(agr,'')
def count(value,agr):
    c=0
    for ip in range(len(value)):
        if agr==value[ip:len(agr)+ip:1]:
            c+=1
    return c        
register.filter('remove',remove)
register.filter('swap',swap)
register.filter('count',count)