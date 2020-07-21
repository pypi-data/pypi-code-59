#!/usr/bin/env python
'''
layout_sheet
Created by Seria at 02/12/2018 1:20 PM
Email: zzqsummerai@yeah.net

                    _ooOoo_
                  o888888888o
                 o88`_ . _`88o
                 (|  0   0  |)
                 O \   。   / O
              _____/`-----‘\_____
            .’   \||  _ _  ||/   `.
            |  _ |||   |   ||| _  |
            |  |  \\       //  |  |
            |  |    \-----/    |  |
             \ .\ ___/- -\___ /. /
         ,--- /   ___\<|>/___   \ ---,
         | |:    \    \ /    /    :| |
         `\--\_    -. ___ .-    _/--/‘
   ===========  \__  NOBUG  __/  ===========
   
'''
# -*- coding:utf-8 -*-

from graphviz import Digraph
from ..law import Law
import os

class BluePrint(object):

    def __init__(self, config=None, verbose=True, hidden=[]):
        if config is None:
            self.param = {'verbose': verbose, 'hidden': hidden}
        else:
            self.param = config
        self.layout_sheet = Digraph(comment='The Space Craft', format='jpg')
        self.layout_sheet.attr('node', shape='doublecircle')
        self.nodes = []
        self.displayed = []
        self._await = False
        self._path = './_'

    def _drawNode(self, prev_node, curr_node, edge_in=None, edge_out=None, init=False, visible=True, if_curr_displayed = False):
        '''
        :param prev_node:
        :param curr_node:
        :param edge: None -> draw an isolated node
        :param init: if it is the first time that prev_node appears in canvas
        :param visible:
        :param if_curr_displayed:
        :return:
        '''
        if prev_node in self.param['hidden'] or curr_node in self.param['hidden']:
            return
        if visible:
            visible = self.param['verbose']
        if len(self.nodes) == 0 and visible:
            print('+' + (63 + len(edge_out)) * '-' + '+')
        if prev_node not in self.nodes:
            self.nodes.append(prev_node)
            if edge_in is None:
                self.layout_sheet.node(prev_node, prev_node, shape='box')
            if init:
                self.layout_sheet.node(prev_node, prev_node, shape='doublecircle')
        if curr_node not in self.nodes:
            self.nodes.append(curr_node)
            if_curr_displayed = True
            self.layout_sheet.node(curr_node, curr_node, shape='box')
        if prev_node != curr_node:
            self.layout_sheet.edge(prev_node, curr_node, label=edge_in)
            if visible and (curr_node not in self.displayed):
                print('| Assembling component\033[34m%32s\033[0m | Output%s |' % (curr_node, edge_out))
                print('+' + (63 + len(edge_out)) * '-' + '+')
            if if_curr_displayed:
                self.displayed.append(curr_node)
        elif visible:
            print('| ReAssembling component\033[34m%30s\033[0m | Output%s |' % (curr_node, edge_out))
            print('+' + (63 + len(edge_out)) * '-' + '+')

    def _combineNodes(self, prev_node, prev_shape, curr_node, symbol):
        self.layout_sheet.node(curr_node+symbol, symbol, shape='circle')
        self.nodes.append(curr_node+symbol)
        self.displayed.append(curr_node+symbol)
        for p in range(len(prev_node)):
            pn = prev_node[p]
            ps = prev_shape[p]
            self._drawNode(pn, curr_node+symbol, ps, visible=False)
        self._drawNode(curr_node+symbol, curr_node, '', visible=False)

    def log(self, log_dir=None, graph_name=None):
        if Law.CORE.upper()=='TENSORFLOW' or self._await:
            if log_dir is None:
                log_dir = os.path.dirname(self._path)
            if graph_name is None:
                graph_name = os.path.basename(self._path)
            gv_name = os.path.join(log_dir, '%s.gv'%graph_name)
            self.layout_sheet.render(gv_name, view=False)
            os.rename(gv_name + '.jpg', os.path.join(log_dir, '%s.jpg'%graph_name))
            os.remove(gv_name)