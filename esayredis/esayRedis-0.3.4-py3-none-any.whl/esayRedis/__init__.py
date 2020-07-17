import asyncio
import fastapi
import pydantic
import uuid
import aredis


class EsayRedis:
    def __init__(self):
        self.redis_pool = None

    async def init_app(
        self,
        app: fastapi.FastAPI = None,
        config: pydantic.BaseSettings = None
    ):

        if config is not None:
            self.config = config
        else:
            self.config = RedisConfig()

        app.state.REDIS = self

        return 0

    async def init(self):
        if self.redis_pool is not None:
            pass
        else:
            self.redis_pool = aredis.ConnectionPool(**self.getconfig())
            await self.conTest()
        # exception handel by redis

    async def Redis(self):

        return aredis.StrictRedis(connection_pool=self.redis_pool)

    async def conTest(self):
        c = await self.Redis()
        value = str(uuid.uuid4())
        r = await c.set('x', value)
        r = await c.get('x')
        print(r)
        assert value == r
        # exception handel by redis

    async def disconnect(self):
        if self.redis_pool is not None:
            self.redis_pool.disconnect()
        else:
            pass

        # exception handel by redis

    def getconfig(self):
        opts = dict(
            host=self.config.redis_host,
            port=self.config.redis_port,
            db=self.config.redis_db,
            max_connections=self.config.redis_pool_maxsize,
            decode_responses=self.config.redis_decode_responses,
            password=self.config.redis_password
        )
        return opts

    def get_redis_address(self) -> str:
        return 'redis://%s:%s/%s' % (
            self.config.redis_host,
            self.config.redis_port,
            self.config.redis_db
        )


class RedisError(Exception):
    pass


class RedisConfig(pydantic.BaseSettings):
    class Config:
        env_prefix = ''
        use_enum_values = True
    redis_host: str = '127.0.0.1'
    redis_port: int = 6379
    redis_password: str = None
    redis_db: int = 4
    redis_connection_timeout: int = 3
    redis_decode_responses = True
    redis_pool_minsize: int = 1
    redis_pool_maxsize: int = 50


esayredis = EsayRedis()
