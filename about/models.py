# -*- coding: utf-8 -*-

from django.db import models

class BlankValueException(Exception):
    'exception for cases when blank value is assigned to no-blank-allowed fields'
    pass

class Biocard(models.Model):
    'little model for displaying about'
    first_name = models.CharField(max_length=100, blank=False)
    second_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=False)
    bio = models.TextField(blank=True, help_text='short biography')
    phone = models.CharField(max_length=15, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    jid = models.CharField(max_length=100, blank=True, help_text='jabber ID')
    twitter = models.CharField(
        max_length=100, 
        blank=True,
        help_text='twitter username'
    )

    def save(self, *args, **kwargs):
        if not self.first_name:
            raise BlankValueException('first name is not allowed to be blank')
        elif not self.last_name:
            raise BlankValueException('last name is not allowed to be blank')
        else:
            super(Biocard, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name

    class Admin: 
        pass
