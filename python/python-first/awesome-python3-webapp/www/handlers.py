#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'lxp'

'''
handlers
'''
import functools
def get(path):
    '''
    Define decorator @get('/path')
    '''
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            return func(*args, **kw)
        wrapper.__method__ = 'GET'
        wrapper.__route__ = path
        return wrapper
    return decorator
  
@get("/api/tt")      
def fn(**kw):
    users = [{'name':'lxp','email':'lxp@qq.com'},{'name':'ldp','email':'ldp@qq.com'}]
    return {
        '__template__': 'test.html',
        'users': users
    }
@get("/")      
def index(**kw):
    print("index")
    for key , value in kw.items():
        print(key)
        print(value)
    #return web.Response(body=b'<h1>index</h1>')
    return "index"
