# -*- coding: utf-8 -*-
from prettysleeper import psleep
from wizprint import fnt
import sys, getopt

def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    time = ''
    alert="Wake up!"
    final=False
    wiz="w"
    helpmsg = f"""{fnt.opt['b']}psleep {fnt.opt['G']}-t time{fnt.opt['c']} {fnt.opt['R']}-a "Wake up!" {fnt.opt['B']}-f False {fnt.opt['c']}{fnt.opt['Y']}-w "w"{fnt.opt['c']}
{fnt.opt['G']}-t --time        {fnt.opt['R']}INTEGER            {fnt.opt['B']}# Time to sleep{fnt.opt['c']}
{fnt.opt['G']}-a --alert       {fnt.opt['R']}SINGLE LETTER      {fnt.opt['B']}# "Message to be printed"{fnt.opt['c']}
{fnt.opt['G']}-f --final       {fnt.opt['R']}BOOLEAN            {fnt.opt['B']}# if True, returns True when completed, Default: no return case{fnt.opt['c']}
{fnt.opt['G']}-w --wiz         {fnt.opt['R']}SINGLE LETTER      {fnt.opt['B']}# Chooses from a set of emoji's build-in; current options:
            "w": "🧙", "p": "👸", "m": "👵", "k": "👴" 
            "x": "🎅", "c": "👮", "d": "🕵", "f": "👩" 
            "a": "👨", "b": "👩", "s": "🦸", "t": "🧚"{fnt.opt['c']}
"""
    try:
       opts, args = getopt.getopt(argv,"ht:a:f:w",["time=","alert=","final=", "wiz="])
    except getopt.GetoptError:
       print(helpmsg)
       sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(helpmsg)
            sys.exit(420)
        elif opt in ("-t", "--time"):
            time = int(arg)
        elif opt in ("-a", "--alert"):
            alert = arg
        elif opt in ("-f", "--final") and type(arg) == type(True):
            final = arg
        elif opt in ("-w", "--wiz"):
            wiz = arg[0:1]
         
    if time != "":
        psleep(time=time, alert=alert, final=final, wiz=wiz)
    else:
        print(helpmsg)

if __name__ == "__main__":
   main()