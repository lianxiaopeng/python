from multiprocessing  import Process
import os 
def run(name):
	print("Run %s (%s) %s" % (name,os.getpid(),__name__))

#if __name__ == '__main__':
#	p = Process(target=run,args=("test",))
#	p.start()
	#p.join()

#print(__name__ )

#认识异步IO
#异步请求多个地址
import asyncio 
import threading
@asyncio.coroutine
def hello():
    print('[hello]begin...(%s)' % threading.currentThread())
    yield from asyncio.sleep(1)
    print('[hello]end..."(%s)' % threading.currentThread())
def wget(host):
    connect = asyncio.open_connection(host,8088)
    reader,writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode("utf-8"))
    yield from writer.drain()
    while True:
        line = yield from  reader.readline()
        if line == b'\r\n':
            break
        print("%s read %s" % (host,line.decode("utf-8")))
    writer.close()
loop = asyncio.get_event_loop()
tasks = [hello(),hello(),wget('172.16.2.23')]

loop.run_until_complete(asyncio.wait(tasks))

loop.close()

