﻿import asyncio

@asyncio.coroutine
def hello():
    print("Hello world!")
    # �첽����asyncio.sleep(1):
    yield from asyncio.sleep(1)
    #print(r)
    print("Hello again!")

# ��ȡEventLoop:
loop = asyncio.get_event_loop()
# ִ��coroutine
loop.run_until_complete(hello())
loop.close()