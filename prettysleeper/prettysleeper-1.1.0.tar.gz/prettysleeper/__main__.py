from .__init__ import psleep
from wizprint import fnt

def main():
    print(f"{fnt.opt['R']}{fnt.opt['b']}How to use this?{fnt.opt['c']}")
    print(f"{fnt.opt['b']}Instead of:{fnt.opt['c']}")
    print(f"{fnt.opt['i']}{fnt.opt['P']}from {fnt.opt['Y']}time {fnt.opt['P']}import{fnt.opt['c']}{fnt.opt['b']} sleep{fnt.opt['c']}")
    print(f"{fnt.opt['b']}.. just use:{fnt.opt['c']}")
    print(f"{fnt.opt['i']}{fnt.opt['P']}from {fnt.opt['Y']}prettysleeper {fnt.opt['P']}import{fnt.opt['c']}{fnt.opt['b']} slpr{fnt.opt['c']}")
    print("")
    print(f"{fnt.opt['b']}Then, in your script where you want to wait 60 seconds{fnt.opt['c']}")
    print("")
    print(f"{fnt.opt['Y']}slpr(60){fnt.opt['c']}")
    print("")
    print(f"{fnt.opt['b']}Will show a timer like:{fnt.opt['c']}")
    try:
        psleep(60)
    except:
        pass

if __name__ == "__main__":
    main()