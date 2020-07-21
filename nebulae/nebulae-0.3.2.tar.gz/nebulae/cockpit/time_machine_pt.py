#!/usr/bin/env python
'''
time_machine_tf
Created by Seria at 04/02/2019 4:35 PM
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
import torch
import os
from glob import glob


class Dock():
    def __init__(self, sd):
        self.scope = '-'.join(sd._spacecraft)
        self._states = {}
        self._craft = {}
        for sc in sd._spacecraft:
            craft = getattr(sd, sc)
            self._craft[sc] = craft
            self._states.update(craft._states)



class TimeMachinePT(object):
    def __init__(self, param):
        '''
        Time Machine saves current states or restores saved states
        '''
        self.param = param

    def _setParams(self, spacedock):
        self.counter = 0
        self.sd = Dock(spacedock)

    def backTo(self, ckpt_scope=None, frozen=False, ins=None, outs=None):
        if self.param['ckpt_path'] is None:
            raise Exception('NEBULAE ERROR ⨷ anchor location is not provided.')
        else:
            if os.path.isfile(self.param['ckpt_path']):
                moment = self.param['ckpt_path']
            else:
                architecture = glob(os.path.join(self.param['ckpt_path'],'*.pth'))
                max_saved = -1
                moment = None
                for arch in architecture:
                    saved_no = int(arch.split('.')[0].split('-')[-1])
                    if saved_no > max_saved:
                        moment = arch
                        max_saved = saved_no
            if moment is None:
                raise Exception('NEBULAE ERROR ⨷ valid anchor is not found.')

            states = torch.load(moment)
            for k, v in states.items():
                s, c = k.split('/')
                sc, sp = s.split(':')
                c = int(c)
                if (ckpt_scope is None) or (not s.startswith(ckpt_scope)):
                    self.sd._craft[sc].comp[c].load_state_dict(v, strict=frozen)
            print('+' + ((10 + len(moment)) * '-') + '+')
            print('| Back to \033[1;34m%s\033[0m |' % moment)
            print('+' + ((10 + len(moment)) * '-') + '+')

    def dropAnchor(self, save_scope=None, frozen=False, anchor=None):
        if self.param['save_path'] is None:
            raise Exception('NEBULAE ERROR ⨷ there is nowhere to drop anchor.')
        else:
            if self.sd.scope:
                scope = self.sd.scope
            else:
                scope = 'ckpt'

            states = self.sd._states
            if save_scope is not None:
                states = {k:v for k,v in states.items() if k.startswith(save_scope)}
            save_ckpt = os.path.join(self.param['save_path'], '%s-%d.pth'%(scope, self.counter))
            torch.save(states, save_ckpt)
            self.counter += 1
            print('| Anchor is dropped at \033[1;34m%s\033[0m |' % save_ckpt)