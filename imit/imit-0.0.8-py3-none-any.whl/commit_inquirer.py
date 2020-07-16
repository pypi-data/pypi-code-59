#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
import os
import inquirer


sys.path.append(os.path.dirname(os.path.realpath(__file__)))  # noqa
import version_handler


def _MsgValidation(answers, current):
    if not current:
        raise inquirer.errors.ValidationError(
            '', reason='Please input commit message!')

    return True


def QType(types):
    question = inquirer.List('commit_type',
                             message='请选择commit类型',
                             choices=types,
                             carousel=True
                             )
    return inquirer.prompt([question])


def QVersion(tags, commit_type, version_file_path):
    tags_index_tagged = []
    nums = list(version_handler.TagNumDict(version_file_path).values())
    index = 0
    for tag in tags:
        tag = '(%d) ' % nums[index] + tag
        index += 1
        tags_index_tagged.append((tag, index))

    current_version = version_handler.CurrentVersion(version_file_path)

    if commit_type == 'modify' or commit_type == 'bugfix':
        index = -1
    elif commit_type == 'feature':
        index = -2
    question = inquirer.List('version_index',
                             message='请选择要增加的版本号(当前: %s)' % current_version,
                             choices=tags_index_tagged,
                             carousel=True,
                             default=tags_index_tagged[index][1]
                             )
    return inquirer.prompt([question])


def QMsg():
    question = inquirer.Text('commit_msg',
                             message='请输入commit message',
                             validate=_MsgValidation
                             )
    return inquirer.prompt([question])
