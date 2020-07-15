#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Usage:
    imit.py [-m|-b|-f|-r] [-1|-2|-3|-4] [-M <msg>] [--log_level=<log_level>]

Options:
    -h,--help                   show usage
    -m                          set commit type: modify
    -b                          set commit type: bugfix
    -f                          set commit type: feature
    -r                          set commit type: revert
    -1                          1st version number +1
    -2                          2nd version number +1
    -3                          3rd version number +1
    -4                          4th version number +1
    -M <msg>                    set commit message
    --log_level=<log_level>     set log level：notset,debug,info,warn,error,fatal,critical
"""

from pprint import pprint
import os
import logging
import sys
import docopt
import inquirer

import version_handler
import commit_inquirer
import option_handler
import git_handler


def main():
    commit_types = {'-m': 'modify',
                    '-b': 'bugfix',
                    '-f': 'feature',
                    '-r': 'revert'}

    version_file_path = 'version.properties'

    if sys.version_info < (3, 7):  # 3.7后dict默认为有序
        raise Exception('Please run with greater than python3.7')

    args = docopt.docopt(__doc__)
    InitLogger(args)
    logging.debug(args)

    commit_option = GetCommitOption(args, commit_types, version_file_path)
    logging.debug('commit option' + str(commit_option))

    git_handler.Handle(commit_option, version_file_path)


def InitLogger(args):
    log_level = args["--log_level"]
    if log_level is None:
        log_level = "debug"  # TODO  INFO

    logging.basicConfig(level=logging._nameToLevel[log_level.upper()],
                        format='[%(levelname)s]: %(message)s')


def GetCommitOption(args, commit_types, version_file_path):
    commit_option = {}
    # 如果版本文件已修改过，则不再修改版本号(index设为0)
    if git_handler.IsFileChanged(version_file_path):
        commit_option['version_index'] = 0

    option_handler.UpdateOptionFromArgs(commit_option, args, commit_types)
    option_handler.UpdateOptionFromInquirer(
        commit_option, version_file_path, commit_types)

    return commit_option


if __name__ == "__main__":
    main()
