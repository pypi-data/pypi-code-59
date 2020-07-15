#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import version_handler
import commit_inquirer
import logging


def _GetCommitType(args, commit_types):
    for i in commit_types:
        if args[i]:
            return commit_types[i]
    return ''


def _GetVersionIndex(args):
    for i in range(1, 5):
        key = '-%d' % i
        if args[key]:
            return i
    return 0


def _GetCommitMsg(args):
    return args['-M']


def UpdateOptionFromArgs(commit_option, args, commit_types):
    commit_type = _GetCommitType(args, commit_types)
    if commit_type and 'commit_type' not in commit_option:
        commit_option['commit_type'] = commit_type

    version_index = _GetVersionIndex(args)
    if version_index > 0 and 'version_index' not in commit_option:
        commit_option['version_index'] = version_index

    commit_msg = _GetCommitMsg(args)
    if commit_msg and 'commit_msg' not in commit_option:
        commit_option['commit_msg'] = commit_msg

    logging.debug('option from args: ' + str(commit_option))


def UpdateOptionFromInquirer(commit_option, version_file_path, commit_types):
    version_dict = version_handler.TagNumDict(version_file_path)
    logging.debug('tag num dict: ' + str(version_dict))

    ci = commit_inquirer.CommitInquirer()

    if 'commit_type' not in commit_option:
        ci.AddType(commit_types.values())

    if 'version_index' not in commit_option:
        ci.AddVersion(version_dict.keys())

    if 'commit_msg' not in commit_option:
        ci.AddMsg()

    answer = ci.GetAnswer()
    logging.debug('option from inquirer: '+str(answer))

    commit_option.update(answer)
