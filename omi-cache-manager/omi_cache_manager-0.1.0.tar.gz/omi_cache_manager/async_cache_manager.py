import logging
import functools
import asyncio
import types

logger = logging.getLogger(__name__)

class AsyncCacheContext():
    def get_cache_context(self):
        "Proxy function for internal cache object."
        raise NotImplementedError
    def create_cache_context(self):
        "Proxy function for internal cache object."
        raise NotImplementedError
    def destory_cache_context(self):
        "Proxy function for internal cache object."
        raise NotImplementedError

class CacheBackend(AsyncCacheContext):
    def config(self, *args, **kwargs):
        "Proxy function for internal cache object."
        raise NotImplementedError

    def clear(self):
        "Proxy function for internal cache object."
        raise NotImplementedError

    def get(self, *args, **kwargs):
        "Proxy function for internal cache object."
        raise NotImplementedError

    def set(self, *args, **kwargs):
        "Proxy function for internal cache object."
        raise NotImplementedError

    def add(self, *args, **kwargs):
        "Proxy function for internal cache object."
        raise NotImplementedError

    def delete(self, *args, **kwargs):
        "Proxy function for internal cache object."
        raise NotImplementedError

    def delete_many(self, *args, **kwargs):
        "Proxy function for internal cache object."
        raise NotImplementedError

    def get_many(self, *args, **kwargs):
        "Proxy function for internal cache object."
        raise NotImplementedError

    def set_many(self, *args, **kwargs):
        "Proxy function for internal cache object."
        raise NotImplementedError

    def execute(self, *args, **kwargs):
        "Proxy function for internal cache object."
        raise NotImplementedError

class SerializableCacheBackend(CacheBackend):
    def load(self, *args, **kwargs):
        "Proxy function for internal cache object."
        raise NotImplementedError

    def dump(self, *args, **kwargs):
        "Proxy function for internal cache object."
        raise NotImplementedError

class AsyncCacheManager:
    def __init__(self, app, cache_backend, config=None):
        if not (config is None or isinstance(config, dict)):
            raise ValueError("`config` must be an instance of dict or None")
        self.config = config
        self.setup_backend(cache_backend,config)
    
    def setup_app(self, app):
        # 为app增加cacha_manager属性
        if isinstance(app,object) and hasattr(app,"state"):
            state = getattr(app,"state")
            if hasattr(state,"cacha_manager"):
                raise ValueError('Can not set cache_manager to an exsit attr [app.state.cacha_manager]')
            else:
                setattr(state,"cacha_manager",self)
        # 保留app的引用
        self._app_ref = app

    def setup_backend(self, cache_backend,config):
        # 如果http_backend是str, 那么反射创建一个CacheBackend的instance
        if isinstance(cache_backend, str):
            name = cache_backend.split('.')
            used = name.pop(0)
            try:
                found = __import__(used)
                # 查找模块下同名classmeta
                for frag in name:
                    used += '.' + frag
                    try:
                        # 使用getattr方式获取type
                        found = getattr(found, frag)
                    except AttributeError:
                        # 使用__import__导入type
                        __import__(used)
                        found = getattr(found, frag)
                # 实例化instance
                cache_backend_instance = found(config = config)
            except ImportError:
                raise ValueError('Cannot resolve cache_backend type %s' % cache_backend)
        else:
            cache_backend_instance = cache_backend
        
        self.cache_backend_name = cache_backend_instance.__class__.__name__
        self.cache = cache_backend_instance

    @property
    def cache_backend(self):
        return self.cache

    def handle_backend_cache_context(self):
        return self.cache.get_cache_context()

    async def create_backend_cache_context(self):
        return await self.async_method_call(
            self.cache.create_cache_context
        )

    async def destory_backend_cache_context(self):
        return await self.async_method_call(
            self.cache.destory_cache_context
        )

    @classmethod
    async def async_method_call(cls, func, *args, **kwargs):
        func_type = type(func)
        if func_type in [types.MethodType,types.FunctionType]:
            func_call = functools.partial(func, *args, **kwargs)
            return await func_call()
        else:
            raise TypeError(f"Function {str(func)} must be FunctionType or MethodType")

    async def clear(self):
        return await self.async_method_call(
            self.cache.clear
        )

    async def get(self, *args, **kwargs):
        return await self.async_method_call(
            self.cache.get,
            *args,
            **kwargs
            )

    async def set(self, *args, **kwargs):
        return await self.async_method_call(
            self.cache.set,
            *args,
            **kwargs
            )

    async def add(self, *args, **kwargs):
        return await self.async_method_call(
            self.cache.add,
            *args,
            **kwargs
            )

    async def delete(self, *args, **kwargs):
        return await self.async_method_call(
            self.cache.delete,
            *args,
            **kwargs
            )

    async def delete_many(self, *args, **kwargs):
        return await self.async_method_call(
            self.cache.delete_many,
            *args,
            **kwargs
            )

    async def get_many(self, *args, **kwargs):
        return await self.async_method_call(
            self.cache.get_many,
            *args,
            **kwargs
            )

    async def set_many(self, *args, **kwargs):
        return await self.async_method_call(
            self.cache.set_many,
            *args,
            **kwargs
            )

    async def execute(self, *args, **kwargs):
         return await self.async_method_call(
            self.cache.execute,
            *args,
            **kwargs
        )
