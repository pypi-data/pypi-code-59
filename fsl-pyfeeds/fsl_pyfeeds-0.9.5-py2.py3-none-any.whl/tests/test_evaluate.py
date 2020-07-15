#!/usr/bin/env python
#
# test_evaluate.py -
#
# Author: Paul McCarthy <pauldmccarthy@gmail.com>
#

import os
import os.path as op

from . import tempdir, makepaths, maketest, makepyfeeds, CaptureStdout

from pyfeeds import testing, evaluate


def test_evaluateTestAgainstBenchmark():
    with tempdir():
        maketest(  'tests/test1/feedsRun',   outputs=['file1', 'file2'])
        maketest(  'tests/test2/feedsRun.1', outputs=['file1', 'file2'])
        maketest(  'tests/test2/feedsRun.2', outputs=['file1', 'file2'])
        os.chmod(  'tests/test1/feedsRun'  , 0o755)
        os.chmod(  'tests/test2/feedsRun.1', 0o755)
        os.chmod(  'tests/test2/feedsRun.2', 0o755)
        os.mkdir('output/')
        os.mkdir('benchmarks/')

        makepaths(['benchmarks/test1/file1',
                   'benchmarks/test1/file2',
                   'benchmarks/test2/1/file1',
                   'benchmarks/test2/1/file2',
                   'benchmarks/test2/2/file1',
                   'benchmarks/test2/2/file2'])

        pyf = makepyfeeds(command='run',
                          testDir=['tests'],
                          outputDir='output',
                          benchmarkDir='benchmarks',
                          overwrite=True)

        for test in pyf.tests:
            assert testing.runTest(pyf,
                                   test,
                                   'output',
                                   None,
                                   'benchmarks',
                                   os.environ.copy(),
                                   False) == (True, 0)

        for resfile in ['output/test1/feedsResults.log',
                        'output/test2/1/feedsResults.log',
                        'output/test2/2/feedsResults.log']:
            assert op.exists(resfile)
            with open(resfile) as f:
                lines = f.readlines()
            lines = [l.strip() for l in lines]
            lines = [l for l in lines if l != '']
            assert len(lines) == 3
            for l in lines[1:]:
                assert 'PASS' in l
