from .__init__ import slpr
from wizprint import wprint, fnt

def main():
    print(f"{fnt.R}{fnt.b}How to use this?{fnt.c}")
    print(f"{fnt.b}Instead of:{fnt.c}")
    print(f"{fnt.i}{fnt.P}from {fnt.Y}time {fnt.P}import{fnt.c}{fnt.b} sleep{fnt.c}")
    print(f"{fnt.b}.. just use:{fnt.c}")
    print(f"{fnt.i}{fnt.P}from {fnt.Y}prettysleeper {fnt.P}import{fnt.c}{fnt.b} slpr{fnt.c}")
    print("")
    print(f"{fnt.b}Then, in your script where you want to wait 60 seconds{fnt.c}")
    print("")
    print(f"{fnt.Y}slpr(60){fnt.c}")
    print("")
    print(f"{fnt.b}Will show a timer like:{fnt.c}")
    try:
        slpr(60)
    except:
        pass

if __name__ == "__main__":
    main()