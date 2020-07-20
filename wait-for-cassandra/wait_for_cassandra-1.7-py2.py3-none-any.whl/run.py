# coding=UTF-8
from __future__ import print_function

import sys
from .base import get_args, get_cluster


def wait(host_name='localhost', wait_timeout=300, login=None, password=None):
    get_cluster(host_name, wait_timeout, login, password)


def load(filename, host_name='localhost', wait_timeout=300, login=None, password=None):
    cluster = get_cluster(host_name, wait_timeout, login, password)
    with open(filename, 'r') as f_in:
        data = f_in.read().replace('\r', ' ').replace('\n', ' ').split(';')
        data = [datum.strip() for datum in data if datum.strip()]

    for query in data:
        cluster.execute(query)


def run():
    if '-l' in sys.argv:
        index = sys.argv.index('-l')
        argv = sys.argv[1:index]+sys.argv[index+2:]
        filename = sys.argv[index+1]
        load(filename, *get_args(argv))
    elif '-h' in sys.argv:
        print('''Use like:

        wait-for-cassandra <hostname>
        wait-for-cassandra <hostname> <wait timeout>
        wait-for-cassandra <hostname> <wait timeout> <login> <password>
        wait-for-cassandra <hostname> -l <file_to_load.cql>
        wait-for-cassandra <hostname> <wait timeout> -l <file_to_load.cql>
        wait-for-cassandra <hostname> <wait timeout> <login> <password> -l <file_to_load.cql>

        Default hostname is localhost, and default timeout is 300 seconds''')
        sys.exit(0)
    else:
        wait(*get_args(sys.argv[1:]))

