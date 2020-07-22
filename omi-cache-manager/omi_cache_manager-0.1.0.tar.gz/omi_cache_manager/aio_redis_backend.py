from functools import wraps
import aioredis
from aioredis import ReplyError
import asyncio
from pydantic import RedisDsn

from .async_cache_manager import CacheBackend

class AIORedisContext():
    def __init__(self,
                redis_uri,
                timeout = 3,
                encoding="utf-8",
                decode_response=True):
        self.redis_uri = redis_uri
        self.timeout = timeout
        self.encoding = encoding
        self._conn_or_pool = None
    
    async def __aenter__(self):   
        if not self._conn_or_pool or self._conn_or_pool.closed:
            await self.create()
        return self._conn_or_pool

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.destory()

    async def create(self):
        self._conn_or_pool = await aioredis.create_redis(
                address=self.redis_uri,
                timeout=self.timeout,
                encoding=self.encoding
        )

    async def destory(self):
        if not self._conn_or_pool:
            return
        self._conn_or_pool.close()
        await self._conn_or_pool.wait_closed()


class AIORedisContextPool(AIORedisContext):
    def __init__(self,
                redis_uri, 
                timeout = 3,
                encoding="utf-8",
                decode_response = True,
                minsize = 0,
                maxsize = 50):
        super().__init__(redis_uri, timeout, encoding, decode_response)
        self.minsize = minsize
        self.maxsize = maxsize

    async def create(self):
        self._conn_or_pool = await aioredis.create_redis_pool(
                    address=self.redis_uri,
                    encoding=self.encoding,
                    minsize=self.minsize,
                    maxsize=self.maxsize,
                    timeout=self.timeout
                )

class AIORedisBackend():        
    def __init__(self, config=None):
        if not (config is None or isinstance(config, dict)):
            raise ValueError("`config` must be an instance of dict or None")
        self._redis_cache_context = None
        self.setup_config(config)

    def setup_config(self,config):
        redis_uri = config.get('CACHE_SCHEME_URI')
        if redis_uri:
            pass
        else:
            redis_uri = RedisDsn.build(
                    scheme=config.get('CACHE_REDIS_SCHEME','redis'),
                    host=config.get('CACHE_REDIS_HOST','localhost'),
                    port=config.get('CACHE_REDIS_PORT','6379'),
                    user=config.get('CACHE_REDIS_USER',''),
                    password=config.get('CACHE_REDIS_PASSWORD',''),
                    path=f"/{config.get('CACHE_REDIS_DATABASE','0') or ''}",
            )

        self.redis_uri = redis_uri
        self.connection_timeout = config.get('CACHE_REDIS_CONNECTION_TIMEOUT',True)
        self.decode_response = config.get('CACHE_REDIS_DECODE_RESPONSE',3)
        self.use_pool = config.get('CACHE_REDIS_USE_POOL',True)
        self.pool_minsize = config.get('CACHE_REDIS_POOL_MINSIZE',1)
        self.pool_maxsize = config.get('CACHE_REDIS_POOL_MAXSIZE',50)

        self.encoding = config.get('CACHE_REDIS_ENCODING','utf-8')
        self.key_prefix=config.get('CACHE_KEY_PREFIX','')

        if not self._redis_cache_context:
            self.create_cache_context()

    def get_cache_context(self):
        return self._redis_cache_context

    def create_cache_context(self):
        if self.use_pool:
            self._redis_cache_context = AIORedisContextPool(
                redis_uri=self.redis_uri,
                timeout= self.connection_timeout,
                encoding=self.encoding,
                decode_response=self.decode_response,
                minsize=self.pool_minsize,
                maxsize=self.pool_maxsize
            )
        else: 
            self._redis_cache_context = AIORedisContext(
                redis_uri=self.redis_uri,
                timeout= self.connection_timeout,
                encoding=self.encoding,
                decode_response=self.decode_response,
            )

    async def destory_cache_context(self):
        if not self._redis_cache_context:
            return
        return await self._redis_cache_context.destory()
    
    def get_async_context(self):
        return self.get_cache_context()

    def make_key(self,key):
        return f"{self.key_prefix}:{key}"

    async def get(self, *args, **kwargs):
        if len(args):
            key = self.make_key(args[0])
        else:
            key = self.make_key(kwargs["key"])
        async with self.get_async_context() as conn:
            return await conn.get(key)

    async def set(self, *args, **kwargs):

        expire=kwargs.get("expire",0)
        pexpire=kwargs.get("pexpire",0)
        exist=kwargs.get("exist",None)

        # 筛选除["expire","pexpire","exist"]以外的key-val
        filter_kv = {k:v for k,v in kwargs.items() if k not in ["expire","pexpire","exist"]}
        if len(args) == 0:
            if len(filter_kv) == 0:
                raise TypeError("Mapping for set might missing, kwargs = %s"%str({**kwargs}))
            elif len(filter_kv) == 1:
                key = list(kwargs.keys())[0]
                value = kwargs[key]
                key = self.make_key(key)
            else:
                raise TypeError("Too many mappings to set, Use set_many method instead of set method, kwargs = %s"%str({**kwargs}))
        elif len(args) == 1:
            if isinstance(args[0], tuple):
                (key,value) = args[0]
                key = self.make_key(key)
            else:
                raise TypeError("Value is required to set key: %s, or paired tuple (key, value)"%str(args[0]))
        elif len(args) == 2:
            key = self.make_key(args[0])
            value = args[1]
        else:
            raise TypeError("Too many keys to set, Use set_many method instead of set method, keys = %s"%str(args))
        
        async with self.get_async_context() as conn:
            result = await conn.set(key=key,
                        value=value,
                        expire=expire,
                        pexpire=pexpire,
                        exist=exist)
        return result

    async def add(self, *args, **kwargs):
        return await self.set(*args, **kwargs)

    async def delete(self, *args, **kwargs):
        if len(args):
            key = self.make_key(args[0])
        else:
            key = self.make_key(kwargs["key"])
        async with self.get_async_context() as conn:
            result = await conn.delete(key=key)
        return result

    async def delete_many(self, *args, **kwargs):
        keys=[]
        for i in range(len(args)):
            key = self.make_key(args[i])
            keys.append(key)
        async with self.get_async_context() as conn:
            result = await conn.delete(*tuple(keys))
        if result > 0:
            return True
        else:
            return False

    async def get_many(self, *args, **kwargs):
        keys = []
        for i in range(len(args)):
            key = self.make_key(args[i])
            keys.append(key)
        async with self.get_async_context() as conn:
            result = await conn.mget(*tuple(keys))
        return result
    
    async def set_many(self, *args, **kwargs):
        kv2update = {
                **{self.make_key(k) : v for k,v in dict(args).items()},
                **{self.make_key(k) : v for k,v in kwargs.items()},
            }
        async with self.get_async_context() as conn:
            result = await conn.mset(kv2update)
        return result

    async def execute(self, *args, **kwargs):
        if len(args) > 0 :
            cmd = args[0]
            args_ex_cmd = args[1:]

        try:
            async with self.get_async_context() as conn:
                if str.lower(cmd) == "get":
                    result =  await self.get(*args_ex_cmd,**kwargs)
                elif str.lower(cmd) == "mget":
                    result =  await self.get_many(*args_ex_cmd,**kwargs)
                elif str.lower(cmd) == "set":
                    result =  await self.set(*args_ex_cmd,**kwargs)
                elif str.lower(cmd) == "mset":
                    result =  await self.set_many(*args_ex_cmd,**kwargs)
                else:
                    result = await conn.execute(*args, **kwargs)
        except ReplyError as ex:
            raise TypeError("Execute command type error,detail=%s"%str(ex))
        return result

    async def clear(self):
        async with self.get_async_context() as conn:
            keys = await conn.keys(self.make_key("*"))
            result = await conn.delete(*tuple(keys))
        return result
