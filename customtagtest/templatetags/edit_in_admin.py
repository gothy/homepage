# -*- coding: utf-8 -*-
from django import template
from django.core.urlresolvers import reverse

register = template.Library()

@register.tag
def edit_in_admin(parser, token):
    'edit_in_admin custom tag. provides edit anchor for model instances in remplates'
    try:
        tag, item = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, \
            "%r tag requires model item param" % token.contents.split()[0]
    return AdminEditModelNode(item)

class AdminEditModelNode(template.Node):
    def __init__(self, item):
        self.item = template.Variable(item)

    def render(self, context):
        try:
            real_item = self.item.resolve(context)
            #this doesn't work in 1.0.2, using a dirty url
            #edit_url = reverse('admin:about_biocard_change', args=(real_item.id,))
            edit_url = '<a href=\"/admin/%s/%s/%s/\">%s</a>' % (
                real_item._meta.app_label,
                real_item._meta.module_name,
                real_item.id,
                '(edit)',
            )
            return edit_url
        except template.VariableDoesNotExist:
            return ''
