# -*- coding: utf-8 -*-

import inspect
import django.db.models
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    'printmodels django management command'
    def handle(self, *args, **options):
        "iterate over app's models and print their names and count in db"
        for mod in django.db.models.get_apps():#get all installed apps' models
            for name in dir(mod):
                m = getattr(mod, name)#convert names to modules
                #if module is a class and is a django model - count and print
                if inspect.isclass(m) and issubclass(m, django.db.models.Model):
                    count = m.objects.count()
                    print m.__module__+'.'+name, count

