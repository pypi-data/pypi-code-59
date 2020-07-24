#!python
# -*- coding:utf-8 -*-

import cPyHiSLIP
import time

def test():
    dev=cPyHiSLIP.HiSLIP("172.28.68.228")
    print dev.ask("*IDN?")
    dev.write(":WAV:SOUR CHAN1;")
    dev.write(":WAV:POIN 1000000;")
    print dev.ask(":WAV:POIN?;")
    dev.write(":SINGLE;")
    while 1:
        dev.ask(":SINGLE;*OPC?")
        dev.write(":WAV:DATA?")
        wf=dev.read()
        #print len(wf)," ",
    del wf
    
if __name__ == "__main__":
    test()
    

