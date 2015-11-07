from orm import User 

import asyncio
from con_pool import create_pool
from aiohttp import web


@asyncio.coroutine
def response_factory(app, handler):
    @asyncio.coroutine
    def response(request):
        # 结果:
        r = yield from handler(request)
        if isinstance(r, web.StreamResponse):
            return r
        if isinstance(r, bytes):
            resp = web.Response(body=r)
            resp.content_type = 'application/octet-stream'
            return resp
        if isinstance(r, str):
            resp = web.Response(body=r.encode('utf-8'))
            resp.content_type = 'text/html;charset=utf-8'
            return resp
        return r
def index(request):
    print("index")
    #return web.Response(body=b'<h1>index</h1>')
    return b'helloworld'
@asyncio.coroutine
def init(loop):
    print('init')
    
    p = yield from create_pool(loop,host='172.16.2.23',user='root',password='root',db='erp_2015')
    app = web.Application(loop = loop,middlewares=[response_factory])
    app.router.add_route("get","/",index)
    srv = yield from loop.create_server(app.make_handler(),'127.0.0.1','9000')
    print(p)
    user = User(id=9,name='lianxiaopeng')
    yield from user.save()
    return srv
    
    
#入口
if __name__ == '__main__':
       
    loop =  asyncio.get_event_loop()
    loop.run_until_complete(init(loop))
    loop.run_forever() 



