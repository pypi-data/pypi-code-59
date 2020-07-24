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

    _cfg = config.get('conf', 'task_temp')
    if not _cfg or not os.path.exists(_cfg):
        logging.error('failed to load the task temp file (%s)' % _cfg)

    with fzip.zip() as _zip:
        from gio import logging_util
        _cw = os.path.dirname(logging_util.log_file)
        _cw = os.path.join(_cw, 'cluster', opts.tag)
        os.path.exists(_cw) or os.makedirs(_cw)
 
        print('tag: %s, num: %s' % (opts.tag, opts.num))
        print('log path: %s' % _cw)

        for _i in range(opts.num):
            print('start task %s/%s' % (_i, opts.num))

            _ks = {'tag': opts.tag, 'i_num': opts.num , 'i_pos': _i, 'cmd': opts.cmd, \
                    't_num': opts.task_num, 'cwd': os.getcwd()}

            _txt = open(_cfg).read()
            _tt = _txt.format(**_ks)

            if opts.print_only:
                print(_tt)
                continue

            _f_tmp = _zip.generate_file('', '.pbs')
            with open(_f_tmp, 'w') as _fo:
                _fo.write(_tt)

            _rs = run_commands.run('qsub ' + _f_tmp, cwd=_cw)
            print(_rs[1])

def usage():
    _p = environ_mag.usage(True)

    _p.add_argument('-c', '--cmd', dest='cmd', required=True)
    _p.add_argument('-t', '--tag', dest='tag', default='default')
    _p.add_argument('-n', '--num', dest='num', type=int, default=1)
    _p.add_argument('-p', '--print-only', dest='print_only', type='bool')
    
    return _p

if __name__ == '__main__':
    from gio import environ_mag
    environ_mag.init_path()
    environ_mag.run(main, [environ_mag.config(usage())]) 