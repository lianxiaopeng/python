import asyncio
from aiohttp import  web


def index(request):
    print('exec index')
    yield from asyncio.sleep(3)
    return web.Response(body=b'<h1>index</h1>')
def hello(request):
    print('exec hello')
    yield from asyncio.sleep(3)
    return web.Response(body=b'<h1>hello</h1>')



@asyncio.coroutine
def server(loop):
    app = web.Application(loop=loop)
    app.router.add_route('Get','/',index)
    app.router.add_route('Get','/hello',hello)
    srv = yield from loop.create_server(app.make_handler(),'127.0.0.1',8000)
    print('Server started at http://127.0.0.1:8000...')
    return srv


loop = asyncio.get_event_loop()    
loop.run_until_complete(server(loop))
loop.run_forever()
