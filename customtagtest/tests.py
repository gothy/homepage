# -*- coding: utf-8 -*-
'test for admin links for model instances'

from django.test import Client
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from views import test_view
from homepage.about.models import Biocard

class SettingsProcessorTestCase(TestCase):
    'tests for settings processor'
    def setUp(self):
        'prepare http client and a card for testing output'
        self.user = User.objects.create_user('user', 'user@host.com', 'pass')
        self.client = Client()
        self.card = Biocard.objects.order_by('id')[0]
        if not self.card:
            self.card, created = Biocard.objects.get_or_create(
                first_name='first', 
                last_name='last'
            )
    
    def tearDown(self):
        User.objects.get(username='user').delete()
    
    def test_response_for_admin_edit_links(self):
        'test output of edit_in_admin tags'
        self.client.login(username='user', password='pass')
        print reverse(test_view)
        response = self.client.get(reverse(test_view))
        self.assertContains(
            response,
            '/admin/about/biocard/%s/' % (self.card.id,),
            count=1, status_code=200
        )
        self.assertContains(
            response,
            '/admin/auth/user/%s/' % (self.user.id,),
            count=1, status_code=200
        )
