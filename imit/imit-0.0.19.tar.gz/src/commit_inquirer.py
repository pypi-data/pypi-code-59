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
        tag += '\t(%d) ' % nums[index]
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


def QJiraId(from_server=False):
    jira_issues = __import__('jira_issues')
    print('正在加载jira 问题列表...')
    issues = []
    if from_server:
        issues = jira_issues.GetJiraIssuesFromServer()
    else:
        issues = jira_issues.GetJiraIssues()
    if not issues:
        print('加载jira 问题列表失败...')
        return {'jira_id': ''}

    jira_ids = []
    for i in issues:  # i[0]is issues id, i[1] is issues summary
        jira_id = i[0]
        jira_summary = i[1]
        if len(jira_summary) > 50:
            jira_summary = jira_summary[:50]+'...'
        jira_ids.append((jira_id + ' ' + jira_summary, jira_id))

    jira_ids.insert(0,  ('无', ''))
    jira_ids.append(('↺【 刷新 】', '--refresh--'))
    question = inquirer.List('jira_id',
                             message='请选择JIRA ID',
                             choices=jira_ids,
                             carousel=True
                             )
    answer = inquirer.prompt([question])
    if answer['jira_id'] == '--refresh--':
        return QJiraId(True)
    else:
        return answer


def QMsg():
    question = inquirer.Text('commit_msg',
                             message='请输入commit message',
                             validate=_MsgValidation
                             )
    return inquirer.prompt([question])


def QUsernamePassword():
    question = [
        inquirer.Text(
            'username', message='请输入Jenkines用户名', validate=lambda _, x: x != ''),
        inquirer.Password('password', message='请输入Jenkines密码',
                          validate=lambda _, x: x != ''),
    ]
    return inquirer.prompt(question)
