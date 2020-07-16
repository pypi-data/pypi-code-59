from random import randint
from time import sleep
sleep(1)
print('''
RandomPlus 1.0.0
Welcome to use randomPlus.We are still under developing.You can use it in Python(Python-3x)''')
def boolrandom():
    from random import randint
    if randint(1,2)==1:
        return True
    else:
        return False
def intrandom(num=1,svm=(1,2)):
    from random import randint
    a=randint(0,len(svm)-1)
    return num+svm[a]
def strandom(text='hello, world'):
    from random import randint
    a=randint(0,len(text)-1)
    return text[a]
def chooserandom(svm=[1,3.14,'hello, world',True]):
    from random import randint
    a=randint(0,len(svm)-1)
    print(svm[a])
def choose_Plus(List=[],length=1,mod='return'):
    i=0
    if length<len(List):
        if mod=='return':
            return IndexError
        elif mod=='modify':
            length=len(List)
        else:
            return None

    x=[]
    while i<length:
        num=randint(0,len(List)-1)
        x.append(List[num])
        List.remove(List[num])
        i+=1
    print(tuple(x))
def help(kw='all'):
    print('''
keywords:
intrandom,
strandom,
boolrandom
''')
    if kw=='intrandom':
        print('intrandom(num,svm):return num+svm[randint],num=int,svm=tuple(all is int)')
    elif kw=='boolrandom':
        print('boolrandom():return True(1/2) or False(1/2)')
    elif kw=='strandom':
        print('strandom(text):return text[randint],text=str')
    elif kw=='chooserandom':
        print('chooserandom(svm):return svm[randint],svm=list or tuple')
    elif kw=='choose_Plus':
        print('''choose_Plus(List,length,mod
do [length] times,choose an element of [List]
mod     return:return Error     modify:length=len(List) if length<len(List) else return None''')
    else:
        print('''
intrandom(num,svm):return num+svm[randint],num=int,svm=tuple(all is int)

boolrandom():return True(1/2) or False(1/2)

strandom(text):return text[randint],text=str

chooserandom(svm):return svm[randint],svm=list or tuple

choose_Plus(List,length,mod
do [length] times,choose an element of [List]
mod     return:return Error     modify:length=len(List) if length<len(List) else return None
''')
