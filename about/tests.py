# -*- coding: utf-8 -*-
'tests for about app'

from django.test import Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from django.test import TestCase
from models import BlankValueException
from models import Biocard
from views import about_view

class BiocardModelTestCase(TestCase):
    'tests for Biocard model'
    def setUp(self):
        'prepare biocards for testing'
        self.card1 = Biocard.objects.create(
                first_name='first',
                second_name='second',
                last_name='last',
        )
        self.card2 = Biocard(first_name='', last_name='last')
        self.card3 = Biocard(first_name='first', last_name=None)
    
    def tearDown(self):
        pass
    
    def test_for_blank(self):
        'test saving of models with blank values which should be filled '
        self.assertRaises(
            BlankValueException, 
            self.card2.save
        )
        self.assertRaises(
            BlankValueException, 
            self.card3.save
        )
    
    def test_unicode_repr(self):
        'test for model\'s correctness in string representation'
        self.assertEquals(unicode(self.card1), 'first last')

class AboutViewTestCase(TestCase):
    'tests for about view'
    def setUp(self):
        'prepare biocard for testing and a client to do requests'
        self.client = Client()
        self.user = User.objects.create_user('user', 'user@host.com', 'pass')
        self.card = Biocard.objects.order_by('id')[0]
        if not self.card:
            self.card, created = Biocard.objects.get_or_create(
                                    first_name='first', 
                                    last_name='last'
                                )
    
    def tearDown(self):
        pass
    
    def test_response(self):
        'testing auth and content containing substring'
        response = self.client.get(reverse(about_view))
        self.assertEqual(response.status_code, 302)#redirect to auth
        self.client.login(username='user', password='pass')
        response = self.client.get(reverse(about_view))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.card.first_name)#check data from fixture
