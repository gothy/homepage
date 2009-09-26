# -*- coding: utf-8 -*-
'tests for LoggingMiddleware'

from django.http import HttpRequest
from django.test import TestCase
from middleware import LoggingMiddleware
from models import BlankValueException
from models import LoggedRequest

class LoggingMiddlewareTestCase(TestCase):
    
    def setUp(self):
        'mock request and prepare middleware for work'
        self.request = HttpRequest()
        self.log_mw = LoggingMiddleware()
    
    def tearDown(self):
        pass
    
    def test_logging_middleware(self):
        'test normal url and method, should be in db after that'
        self.request.path = '/testing/url'
        self.request.method = 'CUSTOM'
        self.log_mw.process_request(self.request)
        log_req = LoggedRequest.objects.get(method=self.request.method)
        self.assertEquals(log_req.path, self.request.path)
        self.assertNotEquals(log_req.timestamp, None)
        
    def test_logging_middleware_with_blank(self):
        'test for blank values. first if path is None, second if method is None'
        self.request.path = None
        self.request.method = 'CUSTOM'
        self.assertRaises(
            BlankValueException, 
            self.log_mw.process_request, self.request
        )
        self.request.path = 'some/url?ololo'
        self.request.method = None
        self.assertRaises(
            BlankValueException, 
            self.log_mw.process_request, self.request
        )
        