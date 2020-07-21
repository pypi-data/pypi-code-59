# coding: utf-8
# ##############################################################################
#  (C) Copyright 2019 Pumpkin, Inc. All Rights Reserved.                       #
#                                                                              #
#  This file may be distributed under the terms of the License                 #
#  Agreement provided with this software.                                      #
#                                                                              #
#  THIS FILE IS PROVIDED AS IS WITH NO WARRANTY OF ANY KIND,                   #
#  INCLUDING THE WARRANTY OF DESIGN, MERCHANTABILITY AND                       #
#  FITNESS FOR A PARTICULAR PURPOSE.                                           #
# ##############################################################################

from typing import List
import serial


class SupMCUSerialMaster:
    def __init__(self, modules: List[str], ports: List[str]):
        self.ports = {}
        ports = [serial.Serial(port, 115200, timeout=.1) for port in ports]
        for port in ports:
            port.write(b'cd SCPI\n')
            port.readlines()
            port.write(b'SUP:RES ERR\n')
            port.readlines()
            port.write(b'SUP:TEL? 0,ASCII\n')
            cmd_name = port.readlines()[-2].split()[1].decode('ascii')
            if cmd_name in modules:
                self.ports[cmd_name] = port
        if any((mod not in self.ports.keys() for mod in modules)):
            bad_mods = [mod for mod in modules if mod not in self.ports.keys()]
            raise IndexError(f"{bad_mods.join(', ')} were not found on the provided ports")

    def send_command(self, mod_name: str, cmd: str):
        if not cmd.endswith('\n'):
            cmd += '\n'
        self.ports[mod_name].write(cmd.encode('ascii'))
        output = self.ports[mod_name].readlines()
        try:
            output = next((line.decode('ascii') for line in output if line.startswith(b'[1')))
            return output.split()[-1].strip('\r\n')
        except StopIteration:
            pass
