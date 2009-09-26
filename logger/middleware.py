# -*- coding: utf-8 -*-
'our custom logging middleware'

from models import LoggedRequest

class LoggingMiddleware:
    'Middleware for logging all passing through request to database'
    
    def __init__(self):
        pass

    def process_request(self, request):
        'saves path,method and timestamp (autodate) to DB'
        logged_req = LoggedRequest()
        logged_req.path = request.path
        logged_req.method = request.method
        logged_req.save()