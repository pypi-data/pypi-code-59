# -*- coding: utf-8 -*-
from time import sleep
from wizprint import fnt

def psleep(time, alert="Wake up!", final=False, wiz="w"):
    """
    slpr(time, alert="Done!")
    time: How many seconds to sleep
    alert: Pass a message to print once done ("Done!" by default)
    final: When set to True, will return True (False by default)
    """
    try:
        try:
            wiz = fnt.emojis.get(wiz) # Try to get a suggested letter
        except:
            wiz = fnt.emojis.get("w") # Get The Wizard if not found
        h = f"{wiz}   " # Header
        chars = ["⇑", "⇗", "⇒", "⇘", "⇓", "⇙", "⇐", "⇖"]
        chars2 = ["🕐", "🕝", "🕓", "🕡", "🕗", "🕤", "🕚", "🕦"]
        charsToUse = chars2
        t = int(time)
        while t != 0:
            for c in charsToUse:
                msg = f"{h}{c} sleeping for {t} "
                bck = "\b" * (len(msg) + 5)
                msg += bck
                print(msg, end="", flush=True)
                howLong = float(1/(len(charsToUse)))
                sleep(howLong)  # 1 sec / 8
            t -= 1
        if final == True:
            return True
    except:
        if final == True:
            return False
    finally:
        msg = " " * 32
        bck = "\b" * 33
        print(msg + bck + h + alert)

