# -*- coding: utf-8 -*-
'Models for logging middleware'

from django.db import models

class BlankValueException(Exception):
    'exception for cases when blank value is assigned to no-blank-allowed fields'
    pass

class LoggedRequest(models.Model):
    'Model for an httprequest basic info'
    path = models.CharField(max_length=255, blank=False)
    method = models.CharField(max_length=10, blank=False, default='GET')
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)
    
    def save(self):
        if not self.path:
            raise BlankValueException('path can\'t be blank')
        elif not self.method:
            raise BlankValueException('method can\'t be blank')
        else:
            super(LoggedRequest, self).save()
    
    def __unicode__(self):
        return "[%s] %s %s" % (self.timestamp, self.method, self.path)