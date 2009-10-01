# -*- coding: utf-8 -*-

from django.db import models
from django.db.models.signals import post_save, post_delete, post_init

#listeners for model creation, saving and deletion
def init_model_listener(sender, instance, **kwargs):
    dblog_helper('created', sender, instance)

def save_model_listener(sender, instance, **kwargs):
    dblog_helper('saved', sender, instance)

def delete_model_listener(sender, instance, **kwargs):
    dblog_helper('deleted', sender, instance)

def dblog_helper(action, sender, instance):
    if sender.__name__ == 'DataAction': return #not logging logs :)
    #print '%s: %s.%s %s' % (action, sender.__module__, sender.__name__, instance)
    
    DataAction.objects.create(
        action_type=action,
        module=sender.__module__,
        name=sender.__name__,
        text_repr=('%s' % instance),
        p_key=('%s' % instance.pk)
    )
#connect to post_* events for all models
post_init.connect(init_model_listener, dispatch_uid='homepage.about')
post_save.connect(save_model_listener, dispatch_uid='homepage.about')
post_delete.connect(delete_model_listener, dispatch_uid='homepage.about')

class BlankValueException(Exception):
    'exception for cases when blank value is assigned to no-blank-allowed fields'
    pass

class Biocard(models.Model):
    'little model for displaying about'
    first_name = models.CharField(max_length=100, blank=False)
    second_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=False)
    birth_date = models.DateField(max_length=10, blank=False, null=True)
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
        return '%s %s' % (self.first_name, self.last_name)

    class Admin: 
        pass

class DataAction(models.Model):
    'django models activity log entry. can include create, save, delete actions'
    action_type = models.CharField(max_length=15, blank=False)
    module = models.CharField(max_length=1000, blank=True)
    name = models.CharField(max_length=100, blank=False)
    text_repr = models.CharField(max_length=300, blank=True)
    p_key = models.CharField(max_length=1000, blank=True)
    action_date = models.DateTimeField(
        auto_now_add=True, 
        max_length=10, 
        blank=False, 
        null=True
    )
    
    def save(self, *args, **kwargs):
        if not self.name:
            raise BlankValueException('name is not allowed to be blank')
        elif not self.action_type:
            raise BlankValueException('action_type is not allowed to be blank')
        else:
            super(DataAction, self).save(*args, **kwargs)

    def __unicode__(self):
        return '%s %s: %s' % (self.action_type, self.name, self.text_repr)

    class Admin: 
        pass
