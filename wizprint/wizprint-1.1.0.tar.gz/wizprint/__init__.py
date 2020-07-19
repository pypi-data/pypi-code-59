# -*- coding: utf-8 -*-
import random
"""
wprint; A Small Gimmick that makes printing tasks to console just a bit more fun by introducing a Wizard that will tell you your customized message in a bubble

wprint("Hello, world!") 

 .://+///:-`   .://+++oo+++++//:-.`-:://////::-
 s+++++++++oo+oo+++++++++++++++++oo+++++++++++os. 
 'o˖˖Hello,˖world!˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖oo
  :/+++///::+ooooooo+os+++++s+oooo+oooooooooooo+/`
                        +o++o+`   `````     ```
                        -s+.
                           🧙

Standard messages show a small bubble, you can expand this however by adding a signature with the option signed="Pythonuigi"
wprint("Hello, Pythonario", signed="Process Peach", wiz="p")

  .://+///:-`  .://+++oo++++//:-.`-:://////::-
   s+++++++++oo+oo++++++++++++++++oo++++++++++os. 
 /s˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖os`
 :s˖˖Hello,˖Pythonario˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖os
 :s˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖os
 'o˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖oo
 .os˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖Process˖Peach˖˖˖˖˖˖˖˖˖oo
 'o˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖oo
  :/+++///::+ooooooo+os+++++s+oooo+oooooooooooo+/`
                        +o++o+`   `````     ```
                        -s+.
                           👸

Try it with:
from wizprint import wprint, fnt
wprint("Hello, Pythonario", signed="Process Peach", wiz="p", background=Y, foreground=R)
All options:
wprint(message="", background=black, foreground=B, bgchar='˖', signed="", wiz="w")

import wizprint.fnt for more font coloring options.

More info on fnt:
    Format console: 
    Colors: # For Blue use B
    (P)urple, (B)lue, (G)reen, (Y)ellow, (R)ed.
    Properties: # For bold use b
    (b)old, (u)nderline, (i)talic, (c)lear
    Example: f"{fnt.opt['B']}Blue {fnt.opt['c']}I am. {fnt.opt['i']}Roses {fnt.opt['c']}{fnt.opt['b']}are {fnt.opt['R']}Red{fnt.opt['c']}"
                Blue /            Clear /           Italic /             Clear /        Bold /              Red /           Clear /

You can find Emoji's in fnt.emojis, I've included a few:
🧙, 👸, 👵, 👴, 🎅, 👮, 🕵, 👩, 👨, 👩, 🦸, 🧚.
"""
class fnt: # Font formatting
    """
Format console: 
Colors: # For Blue use fnt.opt['B']
(P)urple, (B)lue, (G)reen, (Y)ellow, (R)ed.
Properties: # For bold use fnt.opt['b']
(b)old, (u)nderline, (i)talic, (c)lear
Example: f"{fnt.opt['B']}Blue {fnt.opt['c']}I am. {fnt.opt['i']}Roses {fnt.opt['c']}{fnt.opt['b']}are {fnt.opt['R']}Red{fnt.opt['c']}"
            Blue /     Clear /     Italic /      Clear / Bold /      Red /   Clear /

You can find Emoji's in fnt.emojis, I've included a few:
"w": "🧙", "p": "👸", "m": "👵", "k": "👴" 
"x": "🎅", "c": "👮", "d": "🕵", "f": "👩" 
"a": "👨", "b": "👩", "s": "🦸", "t": "🧚"
"""
    opt = {
        "P" : "\033[95m", # Purple
        "B" : "\033[94m", # Blue
        "G" : "\033[92m", # Green
        "Y" : "\033[93m", # Yellow
        "R" : "\033[91m", # Red
        "black" : "\033[90m", # Grey/Black
        "c" : "\033[0m", # Clear formatting
        "b" : "\033[1m", # *Bold*
        "u" : "\033[4m", # _Underline_
        "i" : "\033[3m", # /Italic/
    }
    emojis = {
        "w": "🧙",
        "p": "👸",
        "m": "👵", 
        "k": "👴",
        "x": "🎅",
        "c": "👮",
        "d": "🕵",
        "f": "👩",
        "a": "👨",
        "b": "👩",
        "s": "🦸",
        "t": "🧚",
    }

def wprint(message="", background="black", foreground="B", bgchar='˖', signed="", wiz="w"):
    """
wprint; A Small Gimmick that makes printing tasks to console just a bit more fun by introducing a Wizard that will tell you your customized message in a bubble

wprint("Hello, world!") 

 .://+///:-`   .://+++oo+++++//:-.`-:://////::-
 s+++++++++oo+oo+++++++++++++++++oo+++++++++++os. 
 'o˖˖Hello,˖world!˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖oo
  :/+++///::+ooooooo+os+++++s+oooo+oooooooooooo+/`
                        +o++o+`   `````     ```
                        -s+.
                           🧙

Standard messages show a small bubble, you can expand this however by adding a signature with the option signed="Pythonuigi"
wprint("Hello, Pythonario", signed="Process Peach", wiz="p")

  .://+///:-`  .://+++oo++++//:-.`-:://////::-
   s+++++++++oo+oo++++++++++++++++oo++++++++++os. 
 /s˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖os`
 :s˖˖Hello,˖Pythonario˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖os
 :s˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖os
 'o˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖oo
 .os˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖Process˖Peach˖˖˖˖˖˖˖˖˖oo
 'o˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖˖oo
  :/+++///::+ooooooo+os+++++s+oooo+oooooooooooo+/`
                        +o++o+`   `````     ```
                        -s+.
                           👸

Try it with:
from wizprint import wprint, fnt
wprint("Hello, Pythonario", signed="Process Peach", wiz="p", background=fnt.Y, foreground=fnt.R)
All options:
wprint(message="", background=fnt.black, foreground=fnt.B, bgchar='˖', signed="", wiz="w")

import wizprint.fnt for more font coloring options.
    """
    if message == "":
        message = "Process Toadstool has completed her task and may now continue her journey."
        signed = "Process Peach"
    if signed != "":
        message += f"\n\n\n\t\t\t\t\t{signed}\n"
    # Foreground Selector    
    try:
        foreground = fnt.opt.get(foreground) # Try to get a suggested letter
    except:
        foreground = fnt.opt.get("w") # Get The Wizard if not found
    # Background Selector    
    try:
        background = fnt.opt.get(background) # Try to get a suggested letter
    except:
        background = fnt.opt.get("w") # Get The Wizard if not found
    # Emoji Selector
    try:
        wiz = fnt.emojis.get(wiz) # Try to get a suggested letter
    except:
        wiz = fnt.emojis.get("w") # Get The Wizard if not found
    bgchar = bgchar[0:1:1]
    # Format Message
    header = f"""
 {fnt.opt['black']}   .://+///:-` .://+++oo++++//:-.`-:://////::-   
   s+++++++++oo+oo++++++++++++++++oo++++++++++os.{fnt.opt['c']} """ 
    bubble = [f" {fnt.opt['black']}.o{fnt.opt['c']}--++++++++++++++++++++++++++++++++++++++++--{fnt.opt['black']}y`{fnt.opt['c']}",
    f" {fnt.opt['black']}.os{fnt.opt['c']}-++++++++++++++++++++++++++++++++++++++++--{fnt.opt['black']}oo{fnt.opt['c']}",
    f" {fnt.opt['black']}:s{fnt.opt['c']}--++++++++++++++++++++++++++++++++++++++++--{fnt.opt['black']}os{fnt.opt['c']}",
    f" {fnt.opt['black']}'o{fnt.opt['c']}--++++++++++++++++++++++++++++++++++++++++--{fnt.opt['black']}oo{fnt.opt['c']}",
    f" {fnt.opt['black']}/s{fnt.opt['c']}--++++++++++++++++++++++++++++++++++++++++--{fnt.opt['black']}os`{fnt.opt['c']}",
    f"  {fnt.opt['black']}os{fnt.opt['c']}-++++++++++++++++++++++++++++++++++++++++--{fnt.opt['black']}so.{fnt.opt['c']}",
    f"  {fnt.opt['black']}/s{fnt.opt['c']}-++++++++++++++++++++++++++++++++++++++++-{fnt.opt['black']}oo{fnt.opt['c']}",]
    footer = f"""  {fnt.opt['black']}:/+++///::+ooooooo+os+++++s+oooo+oooooooooooo+/`
         ````````     +o++o+`   `````     ```     
                        -s+.{fnt.opt['c']}  
                           {wiz}"""

    messages = str(message).replace("\t", "    ").replace("\b","").split("\n")
    newMsg = []
    bubbleLen = 40
    for msg in messages:
        while len(msg) > bubbleLen:
            msg1 = msg[:bubbleLen]
            newMsg.append(msg1)
            msg = msg[bubbleLen:]
        newMsg.append(msg)

    finalMsg = []
    if signed != "":
        finalMsg.append(bubble[(random.randint(0,6))])
    for msg in newMsg:
        selectBubble = bubble[(random.randint(0,6))]
        for i in msg:
            if i != " ":
                selectBubble = str(selectBubble.replace('+',  f"{foreground}{fnt.opt['b']}{i}{fnt.opt['c']}", 1))
            else:
                selectBubble = str(selectBubble.replace('+',  "-", 1))
        selectBubble = str(selectBubble).replace('+', '-')
        finalMsg.append(selectBubble)

    userMessage = ""
    for line in finalMsg:
        userMessage += "\n"
        for i in line:
            userMessage += i
    
    userMessage = userMessage.replace('\n', '', 1)
    userMessage = userMessage.replace("-", f"{background}{bgchar}{fnt.opt['c']}").replace("+", f"{background}{bgchar}{fnt.opt['c']}")
    output = ""
    for line in header, userMessage, footer:
        output += "\n"
        for i in line:
            output += i
    output += "\n"

    output = output # .replace("-", f"{background}ʾ{fnt.opt['c']}").replace("+", f"{background}ʾ{fnt.opt['c']}")
    print(output)