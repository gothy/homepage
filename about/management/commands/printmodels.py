# -*- coding: utf-8 -*-

#import inspect
#import django.db.models
from django.db.models.loading import get_models
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    'printmodels django management command'
    def handle(self, *args, **options):
        "iterate over app's models and print their names and count in db"
        for model in get_models():
            print '%s.%s %d' % \
                (model.__module__, model.__name__, model.objects.count())


