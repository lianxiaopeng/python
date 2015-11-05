from orm import User 

import asyncio
from con_pool import create_pool
  
@asyncio.coroutine
def init(loop):
    print('init')
    
    p = yield from create_pool(loop,host='172.16.2.23',user='root',password='root',db='erp_2015')
    print(p)
    user = User(id=4,name='lianxiaopeng')
    yield from user.save()
    
    
#入口
if __name__ == '__main__':
       
    loop =  asyncio.get_event_loop()
    loop.run_until_complete(init(loop))
    loop.run_forever() 



