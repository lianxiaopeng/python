import aiomysql
import asyncio,logging
import config_default

def merge(defaults, override):
    r = {}
    for k, v in defaults.items():
        if k in override:
            if isinstance(v, dict):
                r[k] = merge(v, override[k])
            else:
                r[k] = override[k]
        else:
            r[k] = v
    return r
@asyncio.coroutine
def create_pool(loop, **kw):
    logging.info('create database connection pool...')
    print("create_pool")
    global __pool
    try:
        configs =  config_default.configs
        import config_override
        configs = merge(configs,config_override.configs)
    except ImportError:
        pass
    __pool = yield from aiomysql.create_pool(
        
        
        host=configs.get('host', 'localhost'),
        port=configs.get('port', 3306),
        user=configs['user'],
        password=configs['password'],
        db=configs['db'],
        charset=configs.get('charset', 'utf8'),
        autocommit=configs.get('autocommit', True),
        maxsize=configs.get('maxsize', 10),
        minsize=configs.get('minsize', 1),
        loop=loop
    )
    print(__pool)
    
@asyncio.coroutine
def select(sql, args, size=None):
    log(sql, args)
    global __pool
    with (yield from __pool) as conn:
        cur = yield from conn.cursor(aiomysql.DictCursor)
        yield from cur.execute(sql.replace('?', '%s'), args or ())
        if size:
            rs = yield from cur.fetchmany(size)
        else:
            rs = yield from cur.fetchall()
        yield from cur.close()
        logging.info('rows returned: %s' % len(rs))
        return rs
        
@asyncio.coroutine
def execute(sql, args):
    #log(sql)
    with (yield from __pool) as conn:
        try:
            cur = yield from conn.cursor()
            yield from cur.execute(sql.replace('?', '%s'), args)
            affected = cur.rowcount
            yield from cur.close()
        except BaseException as e:
            raise
        return affected
        
