# -*- coding: utf-8 -*-
'tests for about app'

from django.test import Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from django.test import TestCase
from models import BlankValueException, Biocard
from views import about_view, about_edit_view

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
        User.objects.get(username='user').delete()
    
    def test_response(self):
        'testing auth and content containing substring'
        response = self.client.get(reverse(about_view))
        self.assertEqual(response.status_code, 302)#redirect to auth
        self.client.login(username='user', password='pass')
        response = self.client.get(reverse(about_view))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.card.first_name)#check data from fixture

class AboutEditViewTestCase(TestCase):
    'tests for about edit view'
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
        User.objects.get(username='user').delete()
    
    def test_response(self):
        'testing auth and content containing substring'
        response = self.client.get(reverse(about_edit_view))
        self.assertEqual(response.status_code, 302)#redirect to auth
        self.client.login(username='user', password='pass')
        response = self.client.get(reverse(about_edit_view))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.card.first_name)
        reqdata = {
                  'first_name': 'ololo', 
                  'second_name': 'alala',
                  'last_name': 'ululu',
                  'birth_date': '1986-04-11',
                  'bio': 'biomachine',
                  'phone': '+3800000000',
                  'email': 'thisis@myemail.com',
                  'jid': 'thisis@myjid.com',
                  'twitter': 'impopular'
        }
        response = self.client.post(reverse(about_edit_view), reqdata)
        self.assertNotContains(response, 'This field is required', status_code=302)
        reqdata['first_name'] = ''
        response = self.client.post(reverse(about_edit_view), reqdata)
        self.assertContains(response, 'This field is required', count=1, status_code=200)
        reqdata['last_name'] = ''
        response = self.client.post(reverse(about_edit_view), reqdata)
        self.assertContains(response, 'This field is required', count=2, status_code=200)
        response = self.client.get(reverse(about_view))
        reqdata['first_name'] = 'ololo'
        reqdata['last_name'] = 'alala'
        for key, value in reqdata.items():
            self.assertContains(response, value)

