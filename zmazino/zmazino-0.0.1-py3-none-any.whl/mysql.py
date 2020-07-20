# Python corelib
import configparser, os, logging
from enum import Enum
from typing import Sequence, Callable, Any, AnyStr

# 3rd party lib
from pymysqlpool.pool import Pool

class Error(Enum):
    UNKNOWN_ERROR = -1
    MYSQL_ERROR = -2


class Executor:
    def __init__(self, conf_tag: str, conf_file='config.ini'):
        super().__init__()
        parser = configparser.ConfigParser()

        if os.path.isfile(conf_file):
            parser.read(conf_file)
        else:
            raise FileNotFoundError()

        config = parser[conf_tag]

        username = config['username']
        password = config['password']
        host = config['host']
        port = int(config['port'])
        schema = config['schema']

        try:
            min_size = int(config['minConnection'])
            max_size = int(config['maxConnection'])
        except:
            min_size = 0
            max_size = 10

        self._pool = Pool(user=username, password=password, host=host, port=port,
                          db=schema, min_size=min_size, max_size=max_size)

    def execute(self, query: AnyStr, param: Sequence[Any] = (),
               func: Callable = lambda row: row) -> int:

        try:
            conn = self._pool.get_conn()
            try:
                with conn.cursor() as cursor:
                    count: int = cursor.execute(query, param)
                    conn.commit()
                    rows = cursor.fetchall()
                    for row in rows:
                        func(row)
            except Exception as e:
                count = Error.MYSQL_ERROR
                logging.error(e)
            self._pool.release(conn)
        except Exception as e:
            count = Error.UNKNOWN_ERROR
            logging.error(e)

        return count
    
    def execute_batch(self, query: AnyStr, 
                params: Sequence[Sequence[Any]] = (),
                func: Callable = lambda row: row) -> int:

        try:
            conn = self._pool.get_conn()
            try:
                count = 0
                with conn.cursor() as cursor:
                    for param in params:
                        reg: int = cursor.execute(query, param)
                        count = count + reg
                    conn.commit()
                    rows = cursor.fetchall()
                    for row in rows:
                        func(row)
            except Exception as e:
                count = Error.MYSQL_ERROR
                logging.error(e)
            self._pool.release(conn)
        except Exception as e:
            count = Error.UNKNOWN_ERROR
            logging.error(e)

        return count
