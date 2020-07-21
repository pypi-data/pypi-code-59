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
    def __init__(self, modules: List[str], ports: List[str], default_timeout: int =.1):
        self.ports = {}
        self.timeout = default_timeout
        ports = [serial.Serial(port, 115200, timeout=default_timeout) for port in ports]
        for port in ports:
            port.write(b'cd SCPI\n')
            port.readlines()
            port.write(b'SUP:RES ERR\n')
            port.readlines()
            port.write(b'SUP:TEL? 0,ASCII\n')
            out = self._find_output(port.readlines())
            cmd_name = out.split()[0]
            if cmd_name in modules:
                self.ports[cmd_name] = port
        if any((mod not in self.ports.keys() for mod in modules)):
            bad_mods = [mod for mod in modules if mod not in self.ports.keys()]
            raise IndexError(f"{', '.join(bad_mods)} were not found on the provided ports")

    def send_command(self, mod_name: str, cmd: str, timeout: int = -1):
        if timeout == -1:
            timeout = self.timeout
        self.ports[mod_name].timeout = timeout
        if not cmd.endswith('\n'):
            cmd += '\n'
        self.ports[mod_name].write(cmd.encode('ascii'))
        output = self.ports[mod_name].readlines()
        self.ports[mod_name].timeout = self.timeout
        return self._find_output(output)

    def _find_output(self, output: List[str]) -> str:
        try:
            output = next((line.decode('ascii') for line in output if line.startswith(b'[1')))
            return output.split(maxsplit=1)[-1].strip('\r\n')
        except StopIteration:
            pass
