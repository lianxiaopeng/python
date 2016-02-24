from orm import User 

import asyncio
from con_pool import create_pool
from aiohttp import web
import functools
import inspect
import logging

@asyncio.coroutine
def response_factory(app, handler):
    @asyncio.coroutine
    def response(request):
        logging.info('Response handler...')
        r = yield from handler(request)
        if isinstance(r, web.StreamResponse):
            return r
        if isinstance(r, bytes):
            resp = web.Response(body=r)
            resp.content_type = 'application/octet-stream'
            return resp
        if isinstance(r, str):
            if r.startswith('redirect:'):
                return web.HTTPFound(r[9:])
            resp = web.Response(body=r.encode('utf-8'))
            resp.content_type = 'text/html;charset=utf-8'
            return resp
        if isinstance(r, dict):
            template = r.get('__template__')
            if template is None:
                resp = web.Response(body=json.dumps(r, ensure_ascii=False, default=lambda o: o.__dict__).encode('utf-8'))
                resp.content_type = 'application/json;charset=utf-8'
                return resp
            else:
                resp = web.Response(body=app['__templating__'].get_template(template).render(**r).encode('utf-8'))
                resp.content_type = 'text/html;charset=utf-8'
                return resp
        if isinstance(r, int) and t >= 100 and t < 600:
            return web.Response(t)
        if isinstance(r, tuple) and len(r) == 2:
            t, m = r
            if isinstance(t, int) and t >= 100 and t < 600:
                return web.Response(t, str(m))
        # default:
        resp = web.Response(body=str(r).encode('utf-8'))
        resp.content_type = 'text/plain;charset=utf-8'
        return resp
    return response

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
        
#@get("/api/tt")      
def fn(request):
    #for key , value in kw.items():
    #    print(key)
    #    print(value)
    #return web.Response(body=b'<h1>index</h1>')
    return "ssss";
    
#RequestHandler()(request) = RequestHandler()._func(xp=1) 
# RequestHandler()._func = fn 
# fn = gen("/api/tt")(fn)
#RequestHandler()(request) = gen("/api/tt")(fn)(xp = 1)

class RequestHandler(object):

    def __init__(self, app, fn):
        self._app = app
        self._func = fn
        #...

    @asyncio.coroutine
    def __call__(self, request):
        #kw = ... 获取参数
        r = yield from self._func(xp = 1)
        return r
def add_route(app, fn):
    method = getattr(fn, '__method__', None)
    path = getattr(fn, '__route__', None)
    if path is None or method is None:
        raise ValueError('@get or @post not defined in %s.' % str(fn))
    if not asyncio.iscoroutinefunction(fn) and not inspect.isgeneratorfunction(fn):
        fn = asyncio.coroutine(fn)
    logging.info('add route %s %s => %s(%s)' % (method, path, fn.__name__, ', '.join(inspect.signature(fn).parameters.keys())))
    app.router.add_route(method, path, RequestHandler(app, fn))
        
@asyncio.coroutine
def init(loop):
    print('init')
    
    p = yield from create_pool(loop,host='172.16.2.23',user='root',password='root',db='erp_2015')
    app = web.Application(loop = loop,middlewares=[response_factory])
    
    #add_route(app,fn)
    app.router.add_route('get', '/',fn)
    srv = yield from loop.create_server(app.make_handler(),'127.0.0.1','9000')
    print(p)
    #user = User(id=10,name='lianxiaopeng')
    #yield from user.save()
    return srv
    
    
#入口
if __name__ == '__main__':
       
    loop =  asyncio.get_event_loop()
    loop.run_until_complete(init(loop))
    loop.run_forever() 



