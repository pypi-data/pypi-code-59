import asyncio

import time


def create_interval_retry(init_interval_seconds=7, retry_times=5):
    def decorator(coro_func):
        if asyncio.iscoroutinefunction(coro_func):
            async def new_coro(*args, **kwargs):
                n = 1
                while n <= retry_times:
                    try:
                        task = asyncio.ensure_future(coro_func(*args, **kwargs))
                        return await task
                    except:
                        if n >= retry_times:
                            raise
                        n += 1
                        print('报错')
                        sleep_task = asyncio.ensure_future(asyncio.sleep(init_interval_seconds + n - 1))

                        await sleep_task

            return new_coro
        else:
            def new_func(*args, **kwargs):
                n = 1
                while n <= retry_times:
                    try:
                        return coro_func(*args, **kwargs)
                    except:
                        if n >= retry_times:
                            raise
                        n += 1
                        print('报错')
                        time.sleep(init_interval_seconds + n - 1)

            return new_func

    return decorator


if __name__ == '__main__':
    import random


    # @create_interval_retry()
    # async def f():
    #     c = random.choice([0, 1])
    #     print(f'选择了{c}')
    #
    #     if c == 0:
    #         raise ValueError()
    #
    #
    # asyncio.get_event_loop().run_until_complete(f())

    @create_interval_retry()
    def f():
        c = random.choice([0, 1])
        print(f'选择了{c}')

        if c == 0:
            raise ValueError()


    f()
