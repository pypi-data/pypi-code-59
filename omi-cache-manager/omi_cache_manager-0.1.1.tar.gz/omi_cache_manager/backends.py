import functools
import asyncio

from .async_cache_manager import CacheBackend
from ._decorators import async_method_in_loop

from pydantic import RedisDsn

class NullCacheBackend(CacheBackend):
    def __init__(self, config=None):
        self.config = config
        self.key_prefix=config.get('CACHE_KEY_PREFIX','')
        pass

    @async_method_in_loop
    def get_cache_context(self):
        return None

    @async_method_in_loop
    def create_cache_context(self):
        return None

    @async_method_in_loop
    def destory_cache_context(self):
        return None

    @async_method_in_loop
    def get(self, *args, **kwargs):
        return None

    @async_method_in_loop
    def set(self, *args, **kwargs):
        return True

    @async_method_in_loop
    def add(self, *args, **kwargs):
        return True

    @async_method_in_loop
    def delete(self, *args, **kwargs):
        return True

    @async_method_in_loop
    def delete_many(self, *args, **kwargs):
        return True

    @async_method_in_loop
    def clear(self):
        return None

    @async_method_in_loop
    def get_many(self, *args, **kwargs):
        return None

    @async_method_in_loop
    def set_many(self, *args, **kwargs):
        return True

    @async_method_in_loop
    def execute(self, *args, **kwargs):
        return None


class SimpleCacheDictContext():
    def __init__(self):
        self._cache_dict = dict({"":"","*":""})

    def __enter__(self):
        if not self._cache_dict:
            self.cache_dict = dict({"":"","*":""})
        return self._cache_dict

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    
    async def __aenter__(self):
         # NoOp 
        await asyncio.sleep(0.1)
        if not self._cache_dict:
            self.create()
        return self._cache_dict

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        # NoOp
        await asyncio.sleep(0.1)
        pass
    
    @async_method_in_loop
    def destory(self):
        if not self._cache_dict:
            return 
        self._cache_dict.clear()
        self._cache_dict = None

    @async_method_in_loop
    def create(self):
        self.cache_dict = dict({"":"","*":""})

class SimpleCacheBackend(CacheBackend):
    def __init__(self, config=None):
        self.config = config
        self.key_prefix=config.get('CACHE_KEY_PREFIX','')
        self._cache_context = None
        # setup
        self.setup_config(config)

    def make_key(self,key):
        return f"{self.key_prefix}{key}"

    def setup_config(self, config = None):
        if not self._cache_context:
            self.create_cache_context()

    def get_cache_context(self):
        return self._cache_context

    def create_cache_context(self):
        self._cache_context = SimpleCacheDictContext()

    def destory_cache_context(self):
        if not self._cache_context:
            return
        self._cache_context.destory()

    def get_cache(self):
        with self.get_cache_context() as cache_dict:
            return cache_dict
    
    @async_method_in_loop
    def get(self, *args, **kwargs):
        if len(args) == 1 and len(kwargs) == 0:
            key = self.make_key(args[0])
        elif len(args) == 0 and len(kwargs) == 1:
            key = self.make_key(kwargs["key"])
        else:
            raise TypeError("Too many or no key to get, args = %s kwargs= %s"%(str(args),str({**kwargs})))
        try:
            return self.get_cache().get(key)
        except Exception:
            raise KeyError("Get Key Error, key=%s"%key)

    @async_method_in_loop
    def set(self, *args, **kwargs):
        # 筛选除["expire","pexpire","exist"]以外的key-val
        filter_kv = {k:v for k,v in kwargs.items() if k not in ["expire","pexpire","exist"]}
        cache = self.get_cache()
        if len(args) == 0:
            if len(filter_kv) == 0:
                raise TypeError("Mapping for set might missing, kwargs = %s"%str({**kwargs}))
            elif len(filter_kv) == 1:
                try:
                    kv2update = {self.make_key(k) : v for k,v in kwargs.items()}
                    cache.update(kv2update)
                except KeyError:
                    raise KeyError("Set Key Error, key=%s"%kv2update.keys)
            else:
                raise TypeError("Too many mappings to set, Use set_many method instead of set method, kwargs = %s"%str({**kwargs}))
        elif len(args) == 1:
            if isinstance(args[0], tuple):
                (key,value) = args[0]
                key = self.make_key(key)
            else:
                raise TypeError("Value is required to set key: %s, or paired tuple (key, value)"%str(args[0]))
            try:
                cache[key] = value
            except KeyError:
                raise KeyError("Set Key Error, key=%s"%key)
        elif len(args) == 2:
            key = self.make_key(args[0])
            value = args[1]
            try:
                cache[key] = value
            except KeyError:
                raise KeyError("Set Key Error, key=%s"%key)
        else:
            raise TypeError("Too many keys to set, Use set_many method instead of set method, keys = %s"%str(args))
        return True
    
    @async_method_in_loop
    def delete(self, *args, **kwargs):
        cache = self.get_cache()
        if len(args) == 1 and len(kwargs) == 0:
            key = self.make_key(args[0])
        elif len(args) == 0 and len(kwargs) == 1:
            key = self.make_key(kwargs["key"])
        else:
            raise TypeError("Too many or no key to delete, args = %s kwargs= %s"%(str(args),str({**kwargs})))
        try:
            #查找并删除
            cache.get(key)
            cache.pop(key)
        except Exception:
            raise KeyError("Delete Key Error, key=%s"%key)
        return True

    @async_method_in_loop
    def get_many(self, *args, **kwargs):
        results = []
        cache = self.get_cache()
        if len(args) == 0 :
            raise TypeError("No keys for delete_many, args=%s"%str(args))
        for i in range(len(args)):
            try:
                key = self.make_key(args[i])
                val = cache.get(key)
            except KeyError:
                raise KeyError("Get Key Error, key=%s"%key)
            results.append(val)
        return results

    @async_method_in_loop
    def delete_many(self, *args, **kwargs):
        cache = self.get_cache()
        if len(args) == 0 :
            raise TypeError("No keys for delete_many, keys=%s"%str(args))
        for i in range(len(args)):
            try:
                key = self.make_key(args[i])
                val = cache.get(key)
                if val:
                    cache.pop(key)
            except KeyError:
                raise KeyError("Delete Key Error, key=%s"%key)
        return True

    @async_method_in_loop
    def set_many(self, *args, **kwargs):
        cache = self.get_cache()
        try:
            kv2update = {
                **{self.make_key(k) : v for k,v in dict(args).items()},
                **{self.make_key(k) : v for k,v in kwargs.items()},
            }
            if len(kv2update) > 0:
                cache.update(kv2update)
            else:
                raise TypeError("No keys for get_manay, keys=%s"%kv2update.keys)
        except KeyError:
            raise KeyError("Set Keys Error, keys=%s"%kv2update.keys)
        except ValueError as ex:
            raise ValueError("Error while coverting args to dictionary, set_many supports tuple, but not strings",str(ex))
        return True

    async def add(self, *args, **kwargs):
        # TODO add should return false when key is exist
        return await self.set(*args,**kwargs)

    async def execute(self, *args, **kwargs):
        if len(args) > 0 :
            cmd = args[0]
            args_ex_cmd = args[1:]
        if str.lower(cmd) == "get":
            return await self.get(*args_ex_cmd,**kwargs)
        elif str.lower(cmd) == "mget":
            return await self.get_many(*args_ex_cmd,**kwargs)
        elif str.lower(cmd) == "set":
            return await self.set(*args_ex_cmd,**kwargs)
        elif str.lower(cmd) == "mset":
            return await self.set_many(*args_ex_cmd,**kwargs)
        else:
            raise TypeError("Unimplemented command %s",cmd)

    @async_method_in_loop
    def clear(self):
        cache = self.get_cache()
        if len(cache) > 0:
            cache.clear()
        else:
            return True
        # * => "" and "" => ""
        self.cache = dict({"":"","*":""})
        return True


class RedisContext():
    def __init__(self):
        self._conn_or_pool = None

    def __enter__(self):
        if not self._conn_or_pool:
            self.create()
        return self._conn_or_pool

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self.destory()
    
    async def __aenter__(self):   
        if not self._conn_or_pool:
            await self.create()
        return self._conn_or_pool

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        return await self.destory()

    async def create(self):
        raise NotImplementedError

    async def destory(self):
        raise NotImplementedError


class RedisBackend(CacheBackend):        
    def __init__(self, config=None):
        if not (config is None or isinstance(config, dict)):
            raise ValueError("`config` must be an instance of dict or None")
        self._redis_cache_context = None
        self.setup_config(config)

    def setup_config(self,config):
        self.redis_scheme=config.get('CACHE_REDIS_SCHEME','redis')
        self.redis_host=config.get('CACHE_REDIS_HOST','localhost')
        self.redis_port=config.get('CACHE_REDIS_PORT',6379)
        self.redis_user=config.get('CACHE_REDIS_USER','')
        self.redis_password=config.get('CACHE_REDIS_PASSWORD','')
        self.redis_db=config.get('CACHE_REDIS_DATABASE',0)

        redis_uri = config.get('CACHE_SCHEME_URI')
        if redis_uri:
            pass
        else:
            redis_uri = RedisDsn.build(
                    scheme=self.redis_scheme,
                    host=self.redis_host,
                    port=str(self.redis_port),
                    user=self.redis_user,
                    password=self.redis_password,
                    path=f"/{str(self.redis_db) or ''}"
            )

        self.redis_uri = redis_uri
        self.key_prefix=config.get('CACHE_KEY_PREFIX','')

        if not self._redis_cache_context:
            self.create_cache_context()

    def get_cache_context(self):
        return self._redis_cache_context

    def create_cache_context(self):
        self._redis_cache_context = RedisContext()
    
    async def destory_cache_context(self):
        if not self._redis_cache_context:
            return
        return await self._redis_cache_context.destory()