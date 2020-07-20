import sys
import time

import cassandra
import cassandra.cluster
from cassandra.auth import PlainTextAuthProvider


def get_cluster(host_name='localhost', wait_timeout=300, login=None, password=None):
    start_at = time.time()
    wait_println_counter = 0

    auth_provider = None
    if login is not None and password is not None:
        auth_provider = PlainTextAuthProvider(username=login, password=password)

    while time.time() - start_at < wait_timeout:
        try:
            cluster = cassandra.cluster.Cluster([host_name],
                                                load_balancing_policy=
                                                cassandra.cluster.TokenAwarePolicy(
                                                    cassandra.cluster.DCAwareRoundRobinPolicy(
                                                        local_dc='datacenter1'
                                                    )
                                                ),
                                                auth_provider=auth_provider
                                                )
            return cluster.connect()
        except (cassandra.cluster.NoHostAvailable, cassandra.UnresolvableContactPoints) as e:
            print(repr(e))
            wait_println_counter += 3
            if wait_println_counter == 3:
                print("Waiting 30 more seconds...")
                wait_println_counter = 0
            time.sleep(10)
        else:
            sys.exit(0)
    else:
        print("Waiting time exceeded, aborting...")
        sys.exit(1)


def get_args(argv):

    hostname, timeout, login, password = 'localhost', 300, None, None

    if len(argv) >= 4:
        hostname, timeout, login, password = argv[:4]
    elif len(argv) >= 2:
        hostname, timeout = argv[:2]
    elif len(argv) >= 1:
        hostname, = argv[:1]

    timeout = float(timeout)

    return hostname, timeout, login, password
