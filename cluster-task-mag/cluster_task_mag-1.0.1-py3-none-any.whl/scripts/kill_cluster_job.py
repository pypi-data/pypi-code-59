"""
File: submit_cluster_job.py
Author: Min Feng
Version:  0.1
Create: 2019-12-10 11:15:39
Description: submit a job to the cluster
"""

def main(opts):
    from gio import file_unzip as fzip
    from gio import run_commands
    from gio import config
    import logging
    import os
    import re

    _cs = run_commands.run('qstat')
    _is = []
    for _l in _cs[1].splitlines():
        _m = re.search('^(\S+)\s+(\S+)\s+(\S+)\s+.+', _l)
        if not _m:
            continue

        _i, _n, _u = _m.group(1), _m.group(2), _m.group(3)
        if _u != opts.user:
            continue

        if not (opts.tag in _n):
            continue

        print(_i, _n)
        _is.append(_i)

    if len(_is) <= 0:
        print('found %s jobs' % len(_is))
        return

    _an = input('killing %s jobs? (yes/no) ' % len(_is))
    if _an.lower() not in ('yes', 'y'):
        return

    if opts.print_only:
        print(_cmd)
        return

    _cmd = 'qdel %s' % ' '.join(_is)
    print(run_commands.run(_cmd)[1])

def usage():
    _p = environ_mag.usage(True)

    _p.add_argument('-t', '--tag', dest='tag', required=True)
    _p.add_argument('-u', '--user', dest='user', default='mfeng')
    _p.add_argument('-p', '--print-only', dest='print_only', type='bool')
    
    return _p

if __name__ == '__main__':
    from gio import environ_mag
    environ_mag.init_path()
    environ_mag.run(main, [environ_mag.config(usage())]) 