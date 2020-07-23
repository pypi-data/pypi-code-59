"""
实现能用的异常处理功能


"""

__ALL__ = ['catch', 'catch_all']


def catch_all(log_file=None):
    """
    装饰器的生成函数

    捕捉所有异常并把它写入到 log_file 指定的文件中去，
    如果 log_file == None 那么会在文件 /tmp/ppc-execeptions-YYYY-MM-DDTHH:MM:SS.ssssss.log
    中记录异常。

    Parameters
    ----------
    log_file: str
        日志文件的全路径，如果为 None 就在 /tmp/ 下创建异常日志

    Return
        desc: function
        返回一个装饰器

    """
    def desc(fun):
        """
        给 fun 加上 try except 块

        Parameters
        ----------
        fun: function
            要加上 try except 块的顶层函数
        """
        import logging
        import functools
        from datetime import datetime

        nonlocal log_file

        @functools.wraps(fun)
        def inner_main(*args, **kwargs):
            """
            """
            nonlocal log_file
            if not log_file:
                log_file = "/tmp/ppc-execeptions-{0}.log".format(
                    datetime.now().isoformat())
            logging.basicConfig(filename=log_file)

            try:
                fun(*args, **kwargs)
            except Exception as err:
                logging.exception(err)

        return inner_main

    return desc


catch = catch_all


def test():
    """
    测试用例
    """
    import os

    log_file = "/tmp/ppc-test.log"

    def raise_fun(a, b):
        return a / b

    @catch(log_file)
    def main():
        raise_fun(1, 0)

    main()

    if os.path.isfile(log_file):
        os.remove(log_file)


if __name__ == "__main__":
    test()
