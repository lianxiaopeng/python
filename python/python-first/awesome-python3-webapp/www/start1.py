from orm import User 

import asyncio
from con_pool import create_pool
from aiohttp import web

import inspect
import logging
import os

from jinja2 import Environment,FileSystemLoader


def init_jinja2(app, **kw):
    logging.info('init jinja2...')
    options = dict(
        autoescape = kw.get('autoescape', True),
        block_start_string = kw.get('block_start_string', '{%'),
        block_end_string = kw.get('block_end_string', '%}'),
        variable_start_string = kw.get('variable_start_string', '{{'),
        variable_end_string = kw.get('variable_end_string', '}}'),
        auto_reload = kw.get('auto_reload', True)
    )
    path = kw.get('path', None)
    if path is None:
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
    logging.info('set jinja2 template path: %s' % path)
    env = Environment(loader=FileSystemLoader(path), **options)
    filters = kw.get('filters', None)
    if filters is not None:
        for name, f in filters.items():
            env.filters[name] = f
    app['__templating__'] = env

@asyncio.coroutine
def response_factory(app, handler):
    @asyncio.coroutine
    def response(request):
        print('Response handler...')
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
@asyncio.coroutine
def logger_factory(app, handler):
    print(type(handler))
    @asyncio.coroutine
    def logger(request):
        # 记录日志:
        print('Request: %s %s' % (request.method, request.path))
        logging.info('Request: %s %s' % (request.method, request.path))
        # 继续处理请求:
        return (yield from handler(request))
    return logger
      
    
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

def add_routes(app, module_name):
    n = module_name.rfind('.')
    if n == (-1):
        mod = __import__(module_name, globals(), locals())
    else:
        name = module_name[n+1:]
        mod = getattr(__import__(module_name[:n], globals(), locals(), [name]), name)
    for attr in dir(mod):
        if attr.startswith('_'):
            continue
        fn = getattr(mod, attr)
        if callable(fn):
            method = getattr(fn, '__method__', None)
            path = getattr(fn, '__route__', None)
            if method and path:
                add_route(app, fn)

def add_static(app):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
    app.router.add_static('/static/', path)
    logging.info('add static %s => %s' % ('/static/', path))                
    
    
def datetime_filter(t):
    delta = int(time.time() - t)
    if delta < 60:
        return u'1分钟前'
    if delta < 3600:
        return u'%s分钟前' % (delta // 60)
    if delta < 86400:
        return u'%s小时前' % (delta // 3600)
    if delta < 604800:
        return u'%s天前' % (delta // 86400)
    dt = datetime.fromtimestamp(t)
    return u'%s年%s月%s日' % (dt.year, dt.month, dt.day)

    
@asyncio.coroutine
def init(loop):
    print('init')
    
    p = yield from create_pool(loop,host='172.16.2.23',user='root',password='root',db='erp_2015')
    app = web.Application(loop = loop,middlewares=[response_factory,logger_factory])
    init_jinja2(app, filters=dict(datetime=datetime_filter))

    add_routes(app,'handlers')
    add_static(app)
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
     



