# -*- coding: utf-8 -*-
'tests for processor with django.conf.settings injected in context'

from django.test import Client
from django.test import TestCase
from django.core.urlresolvers import reverse
from contextproc.views import settings_proc_view
from django.conf import settings

class SettingsProcessorTestCase(TestCase):
    'tests for settings processor'
    def setUp(self):
        'prepare http client for testing output'
        self.client = Client()
        settings.TEST_ENV_VAR = 'test me harder!'
    
    def tearDown(self):
        pass
    
    def test_response_for_custom_var(self):
        'test output for custom variable put to django.conf.settings'
        response = self.client.get(reverse(settings_proc_view))
        self.assertContains(
            response,
            unicode(settings.TEST_ENV_VAR),
            count=1, status_code=200
        )
