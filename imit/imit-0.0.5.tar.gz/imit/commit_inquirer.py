#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import inquirer


class CommitInquirer():
    def __init__(self):
        self.questions = []

    def GetQuestions(self):
        return self.questions

    def GetAnswer(self):
        return inquirer.prompt(self.questions)

    # TODO 猜你想输入，作为types的头部插入
    def AddType(self, types):
        question = inquirer.List('commit_type',
                                 message='请选择commit类型',
                                 choices=types,
                                 carousel=True
                                 )
        self.questions.append(question)

    def AddVersion(self, tags, current_version):
        tags_index_tagged = []
        index = 0
        for i in tags:
            index += 1
            tags_index_tagged.append((i, index))

        question = inquirer.List('version_index',
                                 message='请选择要增加的版本号(当前: %s)' % current_version,
                                 choices=tags_index_tagged,
                                 carousel=True
                                 )
        self.questions.append(question)

    def AddMsg(self):
        question = inquirer.Text('commit_msg',
                                 message='请输入commit message',
                                 )
        self.questions.append(question)
