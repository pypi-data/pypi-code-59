#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import git
import logging
from git.cmd import Git

import imit.version_handler as version_handler


def _GitCmd(cmd):
    git = Git(os.getcwd())
    return git.execute(cmd)


def _Add(path):
    cmd = ['git', 'add', path]
    _GitCmd(cmd)


def _Commit(msg):
    cmd = ['git', 'commit', '-m', msg]
    _GitCmd(cmd)


def _GenerateCommitMsg(msg_tags, msg):
    commit_msg = ''
    for i in msg_tags:
        tag = '[%s]' % i
        commit_msg += tag

    commit_msg += ' ' + msg
    return commit_msg


def IsFileChanged(file_name):
    cmd = ['git', 'diff', '--name-only', 'HEAD']
    output = _GitCmd(cmd)
    logging.debug('changed files: ' + str(output))
    changed_files = output.split("\n")
    return file_name in changed_files


def Handle(commit_option, version_file_path):
    version_str_updated = version_handler.Handle(
        commit_option['version_index'], version_file_path)

    msg_tags = [commit_option['commit_type'], version_str_updated]
    commit_msg = _GenerateCommitMsg(msg_tags, commit_option['commit_msg'])
    logging.debug('commit msg: ' + commit_msg)

    _Add(version_file_path)
    _Commit(commit_msg)

    logging.info('commit: ' + commit_msg)


if __name__ == "__main__":
    _Add('test.py')
    print(IsFileChanged('version.properties'))
    _Commit('ABCDQWE')
