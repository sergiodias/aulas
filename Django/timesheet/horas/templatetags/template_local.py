# -*- coding: utf-8 -*-
from django import template
from django.conf import settings
register = template.Library()

@register.filter
def MEDIA_URL(self):
    return settings.MEDIA_URL
