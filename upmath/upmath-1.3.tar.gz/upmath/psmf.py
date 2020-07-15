"""
   Module Name: psmf (precision standard math functions)
   Author:Engr. A.K.M. Aminul Islam
   Date: 2020,July,15
   Version:2.6.2020.07.15
   Late of Last Edit:2020/07/15
   Location:\pmath\psmf.py
   Description:This module includes the standard math functions
	       defined by cpysoft.
	       smf/SMF=Standard Math Functions
               All functions have two versions. Normal precision 
               version and high precision version. High precision
               generating functions have '2' suffix with their 
               name. Like ln(x) gives the value correct to 36 s.f.
	       and ln2(x,prec) is correct to the given precision.
	       Functions are properly validated

               Functions starting with double underscore (__) handles 
               denary number with precision and without input validations

               Functions starting with sinle underscore (__) handles any
               number with precision and with little input validations

               Functions starting without underscore (__) handles any
               number with precision and with full input validations

	       Messages:
		 Non-numeric input:'Input not numeric.'
		 Domain error: 'Check domain of function_name [domain].'

   Dependencies: modules: __future__, upNumber-2.7,pE-2.0,pi-2.0
"""

from __future__ import division
from . import upNumber as upn
from . import pE as pe
from . import pi

__version__="2.6.2020.07.15"



# ------------------------ numeric constants -------------------------
E=pe.getE(prec=36)
e=pe.getE(prec=36)
PI=pi.getPI(prec=36)


# --------------------------- utility functions -----------------------------------
# dataType() function returns the type of a data
# type(2.0) returns "(type 'float')"
def dataType(data=None):
    s=str(type(data)).split(' ')[1]
    return s.split("'")[1]



# ------------------------------- common functions ---------------------------------
# fact(pnum) returns the factorial value of the given precision number object
# >>> smf.fact(10)
# b10:3628800
# >>> smf.fact(upn.Number('1010',2))
# b10:3628800
# >>> smf.fact(upn.Number('i',64))
# b10:6402373705728000
def fact(pnum=None):
    if dataType(pnum)=='int' and pnum>=0:
        return upn.Number(str(__fact(pnum)),10,is_accurate=True)
    elif dataType(pnum)==str(upn.__name__)+'.Number':
        return upn.Number(str(_fact(pnum)),10,is_accurate=True)
    else: raise ValueError("Input is not a positive integer.")

# _fact() returns denary integer, a factorial of a upn number
def _fact(upnum=None):
    if upnum.isInteger() and upnum>=0:
        if upnum.getBase()==10:
            return __fact(int(upnum.getNormalizedPart()['ipart']))
        elif upnum.getBase() in [2,8,16,32,64]:
            return __fact(int(upnum.getBase10Part()['ipart']))
        #return upn.Number(str(num),10,is_accurate=True)
    else: raise ValueError("Arguemnt is not a positive integer UPN for fact().")

# __fact() returns denary integer, factorial of a denary integer
def __fact(num=None):
    if num==0 or num==1:return 1
    p=1
    for i in range(2,num+1):p=p*i
    return p #upn.Number(str(p),10,is_accurate=True)


# -----------------------------Binomial Coefficient-----------------------------
# nCr() returns the upn number of different combinations of different r items 
# from different n items where n>=r
# nCr=n!/r!(n-r)!
def nCr(n=None,r=None):
    if n==None or r==None:
        raise ValueError("Invalid arguement of nCr(n,r).")

    if dataType(n)=='int' and dataType(r)=='int' and n>=0 and r>=0  and n>=r:
        return upn.Number(str(__nCr(n,r)),10,is_accurate=True)
    elif dataType(n)=='int' and dataType(r)==str(upn.__name__)+'.Number' and n>=0 and r>=0 and n>=r:
        if r.getBase()==10:
            if r.getNormalizedPart()['fpart']!='0':
                raise ValueError("Invalid arguments of nCr() function")
            r=int(r.getNormalizedPart()['ipart'])
            return upn.Number(str(__nCr(n,r)),10,is_accurate=True)
        elif r.getBase() in [2,8,16,32,64]:
            if r.getBase10Part()['fpart']!='0':
                raise ValueError("Invalid arguments of nCr() function")
            r=int(r.getBase10Part()['ipart'])
            return upn.Number(str(__nCr(n,r)),10,is_accurate=True)
    elif dataType(n)==str(upn.__name__)+'.Number' and dataType(r)=='int' and n>=0 and r>=0 and n>=r:
        if n.getBase()==10:
            if n.getNormalizedPart()['fpart']!='0':
                raise ValueError("Invalid arguments of nCr() function")
            n=int(n.getNormalizedPart()['ipart'])
            return upn.Number(str(__nCr(n,r)),10,is_accurate=True)
        elif n.getBase() in [2,8,16,32,64]:
            if n.getBase10Part()['fpart']!='0':
                raise ValueError("Invalid arguments of nCr() function")
            n=int(n.getBase10Part()['ipart'])
            return upn.Number(str(__nCr(n,r)),10,is_accurate=True)
    elif dataType(n)==str(upn.__name__)+'.Number' and dataType(r)==str(upn.__name__)+'.Number'\
        and n>=0 and r>=0 and n>=r:
        return upn.Number(str(_nCr(n,r)),10,is_accurate=True)
    else:
        raise ValueError("Invalid arguments of nCr() function")

# _nCr(n,r) returns denary integer of upn numbers n,r where n>=r
def _nCr(n=None,r=None):
    if n.getBase()==10 and r.getBase()==10:
        if n.getNormalizedPart()['fpart']!='0' or r.getNormalizedPart()['fpart']!='0':
            raise ValueError("Invalid arguments of nCr() function")
        n=int(n.getNormalizedPart()['ipart'])
        r=int(r.getNormalizedPart()['ipart'])
        return __nCr(n,r)
    elif n.getBase() in [2,8,16,32,64] and r.getBase()==10:
        if n.getBase10PPart()['fpart']!='0' or r.getNormalizedPart()['fpart']!='0':
            raise ValueError("Invalid arguments of nCr() function")
        n=int(n.getBase10Part()['ipart'])
        r=int(r.getNormalizedPart()['ipart'])
        return __nCr(n,r)
    elif n.getBase()==10 and r.getBase() in [2,8,16,32,64]:
        if n.getNormalizedPart()['fpart']!='0' or r.getBase10Part()['fpart']!='0':
            raise ValueError("Invalid arguments of nCr() function")
        n=int(n.getNormalizedPart()['ipart'])
        r=int(r.getBase10Part()['ipart'])
        return __nCr(n,r)
    elif n.getBase() in [2,8,16,32,64] and r.getBase() in [2,8,16,32,64]:
        if n.getBase10Part()['fpart']!='0' or r.getBase10Part()['fpart']!='0':
            raise ValueError("Invalid arguments of nCr() function")
        n=int(n.getBase10Part()['ipart'])
        r=int(r.getBase10Part()['ipart'])
        return __nCr(n,r)

# __nCr(n,r) returns denary integer of denary integers n,r where n>=r
def __nCr(n=None,r=None):
    if r==0 or r==n:return 1
    if r==1 or r==n-1:return n
    if r>n/2:r=n-r	# nCr=nCn-r
    p=1;j=2		# p=product
    for i in range(n-r+1,n+1):
        p=p*i
        if p%j==0 and j<=r:p=p//j; j=j+1
    return p

# nPr() returns the upn number of different permutations of different r items 
# from different n items where n>=r
# nPr=n!/(n-r)!
def nPr(n=None,r=None):
    if n==None or r==None:
        raise ValueError("Invalid arguement of nPr(n,r).")
    if dataType(n)=='int' and dataType(r)=='int' and n>=0 and r>=0 and n>=r:
        return upn.Number(str(__nPr(n,r)),10,is_accurate=True)
    elif dataType(n)=='int' and dataType(r)==str(upn.__name__)+'.Number'and n>=0 and r>=0 and n>=r:
        if r.getBase()==10:
            if r.getNormalizedPart()['fpart']!='0':
                raise ValueError("Invalid arguments of nPr() function")
            r=int(r.getNormalizedPart()['ipart'])
            return upn.Number(str(__nPr(n,r)),10,is_accurate=True)
        elif r.getBase() in [2,8,16,32,64]:
            if r.getBase10Part()['fpart']!='0':
                raise ValueError("Invalid arguments of nPr() function")
            r=int(r.getBase10Part()['ipart'])
            return upn.Number(str(__nPr(n,r)),10,is_accurate=True)
    elif dataType(n)==str(upn.__name__)+'.Number' and dataType(r)=='int' and n>=0 and r>=0 and n>=r:
        if n.getBase()==10:
            if n.getNormalizedPart()['fpart']!='0':
                raise ValueError("Invalid arguments of nPr() function")
            n=int(n.getNormalizedPart()['ipart'])
            return upn.Number(str(__nPr(n,r)),10,is_accurate=True)
        elif n.getBase() in [2,8,16,32,64]:
            if n.getBase10Part()['fpart']!='0':
                raise ValueError("Invalid arguments of nPr() function")
            n=int(n.getBase10Part()['ipart'])
            return upn.Number(str(__nPr(n,r)),10,is_accurate=True)
    elif dataType(n)==str(upn.__name__)+'.Number' and dataType(r)==str(upn.__name__)+'.Number' and\
        n>=0 and r>=0 and n>=r:
        return upn.Number(str(_nPr(n,r)),10,is_accurate=True)
    else:
        raise ValueError("Invalid arguments of nPr() function")

# _nPr(n,r) returns denary integer of upn numbers n,r where n>=r
def _nPr(n=None,r=None):
    if n.getBase()==10 and r.getBase()==10:
        if n.getNormalizedPart()['fpart']!='0' or r.getNormalizedPart()['fpart']!='0':
            raise ValueError("Invalid arguments of nPr() function")
        n=int(n.getNormalizedPart()['ipart'])
        r=int(r.getNormalizedPart()['ipart'])
        return __nPr(n,r)
    elif n.getBase() in [2,8,16,32,64] and r.getBase()==10:
        if n.getBase10Part()['fpart']!='0' or r.getNormalizedPart()['fpart']!='0':
            raise ValueError("Invalid arguments of nPr() function")
        n=int(n.getBase10Part()['ipart'])
        r=int(r.getNormalizedPart()['ipart'])
        return __nPr(n,r)
    elif n.getBase()==10 and r.getBase() in [2,8,16,32,64]:
        if n.getNormalizedPart()['fpart']!='0' or r.getBase10Part()['fpart']!='0':
            raise ValueError("Invalid arguments of nPr() function")
        n=int(n.getNormalizedPart()['ipart'])
        r=int(r.getBase10Part()['ipart'])
        return __nPr(n,r)
    elif n.getBase() in [2,8,16,32,64] and r.getBase() in [2,8,16,32,64]:
        if n.getBase10Part()['fpart']!='0' or r.getBase10Part()['fpart']!='0':
            raise ValueError("Invalid arguments of nPr() function")
        n=int(n.getBase10Part()['ipart'])
        r=int(r.getBase10Part()['ipart'])
        return __nPr(n,r)

# __nPr(n,r) returns denary integer of denary integers n,r where n>=r
def __nPr(n=None,r=None):
    #if r>n:raise ValueError("Invalid arguments of __nPr() function")
    if r==0:return 1
    elif r==1:return n
    elif r==n:return __fact(n)
    p=1
    for i in range(n-r+1,n+1):
        p=p*i    
    return p

# ----------------------- End of Binomial Coefficients---------------------



# ----------------------- logarithmic function -----------------------------
# ln2(prec) returns the natural logarithm of ln2 correct to the 
# given precision value
# ln2(100)=0.6931471805599453094172321214581765680755001343602552541206
#            800094933936219696947156058633269964186875

# it takes 0.02008 s in 32 bit system for 36 prec
def ln2(prec=36):
    if dataType(prec)!='int' or prec<1: prec=36
    delP=upn.Number('1p-'+str(prec),10,prec=prec)

    if prec<100: prec2=prec+4
    else:prec2=int(1.05*prec)

    SUM=upn.Number('0.0',10,prec=prec2);
    t=upn.Number('1.0',10,prec=prec2)
    i=0;m=1
    while(t >= delP):        
        t=upn.Number(str(3*(2*i+1)*m),base=10,prec=prec2)
        t=2/t;
        SUM=SUM+t
        m=m*9; i=i+1
    return SUM.createNewNumber(prec,False)

# __ln2(prec) calculates the natural logarithm of denary 2 correct
# the given precision+excess digits
def __ln2(prec=36):
    delP=upn.Number('1p-'+str(prec),10,prec=prec,is_accurate=True)
    if prec<100: prec2=prec+4
    else:prec2=int(1.05*prec)
    SUM=upn.Number('0.0',10,prec=prec2,is_accurate=False);
    t=upn.Number('1.0',10,prec=prec2,is_accurate=False)
    i=0;m=1
    while(t >= delP):        
        t=upn.Number(str(3*(2*i+1)*m),base=10,prec=prec2)
        t=2/t;
        SUM=SUM+t
        m=m*9; i=i+1
    return SUM.createNewNumber(prec2*2,False)

# it takes 0.03414 s in 32 bit system for 36 prec
def ln3(prec=36):
    if dataType(prec)!='int' or prec<1: prec=36
    delP=upn.Number('1p-'+str(prec),10,prec=prec)

    if prec<100: prec2=prec+4
    else:prec2=int(1.05*prec)

    SUM=upn.Number('0',10,prec=prec2);
    t=upn.Number('1.0',10,prec=prec2)
    i=0;m=2
    while(t > delP):
        t=1/upn.Number(str(m*(2*i+1)),10,prec=prec2)
        SUM=SUM+1/upn.Number(str(m*(2*i+1)),10,prec=prec2)
        m=m*4;i=i+1
    SUM=2*SUM
    return SUM.createNewNumber(prec2*2,False)

# ln2_cfm2(prec) calculates natural logarithm of denary number
# 2 by continued fraction method (cfm)
# ln2=0.6931471805599453094172321214581765680755001343602552541206
#       800094933936219696947156058633269964186875
def ln2_cfm(prec=36):
    if dataType(prec)!='int' or prec<1: prec=36
    delP=upn.Number('1p-'+str(prec),10,prec=prec)

    if prec<100: prec2=prec+4
    else:prec2=int(1.05*prec)

    def denoFunc(i,prec):
        t1=upn.Number(str(6*i-3),base=10,prec=prec)
        t2=upn.Number(str(6*i+3),base=10,prec=prec)
        return t1-(i*i/t2)

    i=prec//3;
    while True:
        deno=denoFunc(i,prec2)
        for j in range(i-1,0,-1):
            deno=upn.Number(str(6*j-3),base=10,prec=prec)-j*j/deno
        num1=2/deno
        i=i+1
        deno=denoFunc(i,prec2)
        for j in range(i-1,0,-1):
            deno=upn.Number(str(6*j-3),base=10,prec=prec)-j*j/deno
        num2=2/deno
        if num2-num1 < delP:break
        i=i+prec//3;
    return num2.createNewNumber(prec,False)

# __ln2_cfm(prec) calculates the natural logarithm of denary 2 correct
# to the given precision by continued fraction method
def __ln2_cfm(prec=36):
    delP=upn.Number('1p-'+str(prec),10,prec=prec)

    if prec<100: prec2=prec+4
    else:prec2=int(1.05*prec)

    def denoFunc(i,prec):
        t1=upn.Number(str(6*i-3),base=10,prec=prec2)
        t2=upn.Number(str(6*i+3),base=10,prec=prec2)
        return t1-(i*i/t2)

    i=prec//3;
    while True:
        deno=denoFunc(i,prec2)
        for j in range(i-1,0,-1):
            deno=upn.Number(str(6*j-3),base=10,prec=prec2)-j*j/deno
        num1=2/deno
        i=i+1
        deno=denoFunc(i,prec2)
        for j in range(i-1,0,-1):
            deno=upn.Number(str(6*j-3),base=10,prec=prec2,is_accurate=False)-j*j/deno
        num2=2/deno
        if num2-num1 < delP:break
        i=i+prec//3;
    return num2.createNewNumber(prec2*2,False)

# __ln10_cfm(prec) calculates the natural logarithm of denary 10 correct
# to the given precision by continued fraction method
def __ln10_cfm(prec=36):
    delP=upn.Number('1p-'+str(prec),10,prec=prec)

    if prec<100: prec2=prec+4
    else:prec2=int(1.05*prec)

    def denoFunc1(i,prec):
        t1=upn.Number(str(18*i-9),base=10,prec=prec)
        t2=upn.Number(str(18*i+9),base=10,prec=prec)
        return t1-(i*i/t2)

    def denoFunc2(i,prec):
        t1=upn.Number(str(506*i-253),base=10,prec=prec)
        t2=upn.Number(str(506*i+253),base=10,prec=prec)
        return t1-(9*i*i/t2)

    i=prec//3;
    while True:
        deno=denoFunc1(i,prec2)
        for j in range(i-1,0,-1):
            deno=upn.Number(str(18*j-9),base=10,prec=prec)-j*j/deno
        m1=20/deno
        deno=denoFunc2(i,prec2)
        for j in range(i-1,0,-1):
            deno=upn.Number(str(506*j-253),base=10,prec=prec)-9*j*j/deno
        m2=18/deno
        num1=m1+m2
        i=i+1
        deno=denoFunc1(i,prec2)
        for j in range(i-1,0,-1):
            deno=upn.Number(str(18*j-9),base=10,prec=prec)-j*j/deno
        n1=20/deno
        deno=denoFunc2(i,prec2)
        for j in range(i-1,0,-1):
            deno=upn.Number(str(506*j-253),base=10,prec=prec,is_accurate=False)-9*j*j/deno
        n2=18/deno
        num2=n1+n2

        if num2-num1 < delP:break
        i=i+prec//3;
    return num2.createNewNumber(prec2*2,False)


# --------------------------- start of ln_cfm() ----------------------------------
# ln_cfm(x,prec) calculates the natural logarithm of 'pNumber' x
# by continued fraction method correct to the given precision
# >>> smf.ln_cfm(10)
# b10:2.302585092994045684017991454684364206
# >>> smf.ln_cfm(5.75)
# b10:1.749199854809259071972288588893842982
# >>> smf.ln_cfm(-0.5)
# b10:<UNDEFINED>
# >>> smf.ln_cfm(0.5)
# b10:-0.693147180559945309417232121458176568
# >>> smf.ln_cfm(0)
# b10:<-INF>
# >>> smf.ln_cfm(upn.Number('100',2,prec=36))
# b10:1.386294361119890618834464242916353136
def ln_cfm(x=None,prec=36):
    if dataType(prec)!='int' or prec<0: prec=36
    if dataType(x) not in ['int','float',str(upn.__name__)+'.Number']:
        raise ValueError("Invalid argument of function ln_cfm()")
    if dataType(prec)!='int' or prec<1: prec=36
    if x==0:return upn.Number('<-inf>',10,0,is_accurate=True)
    elif x<0:return upn.Number('<undefined>',10,0,is_accurate=True)
    elif x==1:return upn.Number('0',base=10,prec=1,is_accurate=True)
    elif x==e or x==E:return upn.Number('1',base=10,prec=1,is_accurate=True)

    if dataType(x) in ['int','float']:
        x=upn.Number(str(x),base=10,prec=prec,is_accurate=False)
        num=_ln_cfm(x,prec=prec)
    elif dataType(x)==str(upn.__name__)+'.Number':num=_ln_cfm(x,prec=prec)

    return num.createNewNumber(prec,False)


# _ln_cfm(x,prec) calculates the natural logarithm of 'pNumber' x
# by continued fraction method correct to the given precision
# >>> smf._ln_cfm(upn.Number('10000.11',2,36))
# b10:2.818398258271075440835607753447369614
def _ln_cfm(x=None,prec=36):
    if dataType(x)!=str(upn.__name__)+'.Number':
        raise ValueError("Arguement is not a Number instance.")

    if x==0:return upn.Number('<-inf>',10,0,is_accurate=True)
    elif x<0:return upn.Number('<undefined>',10,0,is_accurate=True)
    elif x==0.5 or x==1/2: return -1*__ln2(prec)
    elif x==1:return upn.Number('0',base=10,prec=prec,is_accurate=True)
    elif x==2:return ln2(prec)
    elif x==e or x==E:return upn.Number('1',base=10,prec=prec,is_accurate=True)
    elif x==10:return __ln10_cfm(prec)
    elif x==4:return __ln2(prec)*2
    elif x==8:return __ln2(prec)*3
    elif x==16:return __ln2(prec)*4
    elif x==32:return __ln2(prec)*5
    elif x==64:return __ln2(prec)*6 

    delP=upn.Number('1p-'+str(prec),10,prec=prec,is_accurate=True)
    if prec<100: prec2=prec+8
    else:prec2=int(1.2*prec)

    # private function
    def denoFunc(a,i,prec):
        t1=upn.Number(str((2*i-1)*(a+4))[4:],base=10,prec=prec2)
        t2=upn.Number(str((2*i+1)*(a+4))[4:],base=10,prec=prec2)
        return t1-(i*i*a*a/t2)

    # converting x to 1+a/b; where b=2
    a=2*(x-1)
    i=prec//3
    while True:
        deno=denoFunc(a,i,prec2);
        for j in range(i-1,0,-1):
            deno=upn.Number(str((2*j-1)*(a+4))[4:],base=10,prec=prec2)-j*j*a*a/deno
        num1=2*a/deno
        i=i+1
        deno=denoFunc(a,i,prec2);
        for j in range(i-1,0,-1):
            deno=upn.Number(str((2*j-1)*(a+4))[4:],base=10,prec=prec2,is_accurate=False)-j*j*a*a/deno
        num2=2*a/deno
        if num2-num1 < delP:break
        i=i+prec//3;
    return num2.createNewNumber(prec2*2,False)

# __ln_cfm(x,prec) calculates the natural logarithm of 'denary' x
# by continued fraction method correct to the given precision
# >>> smf.__ln_cfm(16.75)
# b10:2.818398258271075440835607753447369614
def __ln_cfm(x=None,prec=36):
    if x==0:return upn.Number('<-inf>',10,0,is_accurate=True)
    elif x<0:return upn.Number('<undefined>',10,0,is_accurate=True)
    elif x==0.5 or x==1/2: return -1*__ln2(prec)
    elif x==1:return upn.Number('0',base=10,prec=prec,is_accurate=True)
    elif x==2:return ln2(prec)
    elif x==e or x==E:return upn.Number('1',base=10,prec=prec,is_accurate=True)
    elif x==10:return __ln10_cfm(prec)
    elif x==4:return __ln2(prec)*2
    elif x==8:return __ln2(prec)*3
    elif x==16:return __ln2(prec)*4
    elif x==32:return __ln2(prec)*5
    elif x==64:return __ln2(prec)*6 

    delP=upn.Number('1p-'+str(prec),10,prec=prec)
    if prec<100: prec2=prec+8
    else:prec2=int(1.2*prec)

    # private function
    def denoFunc(a,i,prec):
        t1=upn.Number(str((2*i-1)*(a+4))[4:],base=10,prec=prec2)
        t2=upn.Number(str((2*i+1)*(a+4))[4:],base=10,prec=prec2)
        return t1-(i*i*a*a/t2)

    # converting x to 1+a/b; where b=2
    x=upn.Number(str(x),base=10,prec=prec2,is_accurate=False)
    a=2*(x-1)
    i=prec//3
    while True:
        deno=denoFunc(a,i,prec2)
        for j in range(i-1,0,-1):
            deno=upn.Number(str((a+4)*(2*j-1))[4:],base=10,prec=prec2)-j*j*a*a/deno
        num1=2*a/deno
        i=i+1
        deno=denoFunc(a,i,prec2)
        for j in range(i-1,0,-1):
            deno=upn.Number(str((a+4)*(2*j-1))[4:],base=10,prec=prec2,is_accurate=False)-j*j*a*a/deno
        num2=2*a/deno
        if num2-num1 < delP:break
        i=i+prec//3;

    return num2.createNewNumber(prec2*2,False)
# ---------------------------- End of ln_cfm() ----------------------------------


# ----------------------------- start of ln() -----------------------------------
def ln(x=None,prec=36):
    if x==None:raise ValueError("Invalid arguement of ln(x,prec).")
    if dataType(prec)!='int' or prec<0: prec=36
    if dataType(x) not in ['int','float',str(upn.__name__)+'.Number']:
        raise ValueError("Invalid argument of function ln(x,prec)")
    if dataType(prec)!='int' or prec<1: prec=36
    if x==0:return upn.Number('<-inf>',10,0,is_accurate=True)
    elif x<0:return upn.Number('<undefined>',10,0,is_accurate=True)
    elif x==1:return upn.Number('0',base=10,prec=1,is_accurate=True)
    elif x==e or x==E:return upn.Number('1',base=10,prec=1,is_accurate=True)

    if dataType(x) in ['int','float']:num=__ln(x,prec=prec)
    elif dataType(x)==str(upn.__name__)+'.Number':num=_ln(x,prec=prec)
    return num.createNewNumber(prec,is_accurate=False)


# _ln(x,prec) calculates the natural logarithm of 'pNumber' x
# correct to the given precision by calling __ln(x,prec)
def _ln(x=None,prec=36):
    if dataType(x)!=str(upn.__name__)+'.Number':
        raise ValueError("Arguement is not a Number instance.")

    if x==0:return upn.Number('<-inf>',10,0,is_accurate=True)
    elif x<0:return upn.Number('<undefined>',10,0,is_accurate=True)
    elif x==0.5 or x==1/2: return -1*__ln2(prec)
    elif x==1:return upn.Number('0',base=10,prec=1,is_accurate=True)
    elif x==2:return __ln2(prec)
    elif x==e or x==E:return upn.Number('1',base=10,prec=1,is_accurate=True)
    elif x==10:return __ln10_cfm(prec)
    elif x==8:return __ln2(prec)*3
    elif x==16:return __ln2(prec)*4
    elif x==32:return __ln2(prec)*5
    elif x==64:return __ln2(prec)*6

    delP=upn.Number('1p-'+str(prec),10,prec=prec,is_accurate=True)
    if prec<100: prec2=prec+4
    else:prec2=int(1.05*prec)

    # A large number is reduced to smaller one
    # x=2^n*a; ln(x)=nln(2) + ln(a)
    n=0
    if x>2:
        while(x>2):
            x=x/2
            n=n+1            
    elif x<1 and x>0:
        while(x<1):
            x=x*2
            n=n-1

    if x!=0 or x!=0.0:num=n*__ln2(prec=prec2)+_ln_cfm(x,prec=prec2)
    else:num=n*__ln2(prec=prec2)        
    return num.createNewNumber(prec2*2,is_accurate=False)
        

# __ln(x,prec) calculates the natural logarithm of denary number, x
# correct to the given precision
def __ln(x=None,prec=36):
    if dataType(prec)!='int': prec=36

    if x==0:return pn.Number('<-inf>',10,0,is_accurate=True)
    elif x<0:return pn.Number('<undefined>',10,0,is_accurate=True)
    elif x==0.5 or x==1/2: return -1*__ln2(prec)
    elif x==1:return pn.Number('0',base=10,prec=1,is_accurate=True)
    elif x==2:return __ln2(prec)
    elif x==e or x==E:return pn.Number('1',base=10,prec=1,is_accurate=True)
    elif x==10:return __ln10_cfm(prec)
    elif x==8:return __ln2(prec)*3
    elif x==16:return __ln2(prec)*4
    elif x==32:return __ln2(prec)*5
    elif x==64:return __ln2(prec)*6

    delP=upn.Number('1p-'+str(prec),10,prec=prec,is_accurate=True)
    if prec<100: prec2=prec+4
    else:prec2=int(1.05*prec)

    # A large number is reduced to smaller one
    # x=2^n*a; ln(x)=nln(2) + ln(a)
    n=0
    if x>2:
        while(x>2):
            x=x/2
            n=n+1            
    elif x<1 and x>0:
        while(x<1):
            x=x*2
            n=n-1

    if x!=0 or x!=0.0:num=n*__ln2(prec=prec2)+__ln_cfm(x,prec=prec2)
    else:num=n*__ln2(prec=prec2)        
    return num.createNewNumber(prec2*2,is_accurate=False)
# ----------------------------- end of ln() -----------------------------------



# ----------------------------- start of lg() -----------------------------------
# lg(x,prec) returns the 10 based logarithm of precision number object x, 
# correct to the given precision
# >>> smf.lg(16.75)
# b10:1.224014811372864043721653839777082527
def lg(x=None,prec=36):
    if x==None:raise ValueError("Invalid arguement of ln(x,prec).")
    if dataType(x) not in ['int','float',str(upn.__name__)+'.Number']: 
        raise SyntaxError('Input not numeric.')
    if dataType(prec)!='int' or prec<1: prec=36
    if x==0:return upn.Number('<-inf>',10,0,is_accurate=True)
    elif x<0:return upn.Number('<undefined>',10,0,is_accurate=True)
    elif x==1:return upn.Number('0',base=10,prec=prec,is_accurate=True)
    elif x==10:return upn.Number('1',base=10,prec=prec,is_accurate=True)

    if dataType(x) in ['int','float']:
        if x==e or x==E:num=1/__ln10_cfm(prec)
        elif x==0.5 or x==1/2: num=-1*__lg2(prec)
        elif x==2:num=__lg2(prec)
        elif x==4:num=__lg2(prec)*2
        elif x==8:num=__lg2(prec)*3
        elif x==16:num=__lg2(prec)*4
        elif x==32:num=__lg2(prec)*5
        elif x==64:num=__lg2(prec)*6
        else: num=__lg(x,prec)
    elif dataType(x)==str(upn.__name__)+'.Number':
        # A large number is reduced to smaller one
        # x=10^n*a; lg(x)=n + lg(a)
        n=0
        if x>10:
            while(x>=10):
                x=x/10
                n=n+1
            if x==1:return upn.Number(str(n),base=10,prec=prec,is_accurate=True)
        elif x<1 and x>0:
            while(x<1):
                x=x*10
                n=n-1
            if x==1:return upn.Number(str(n),base=10,prec=prec,is_accurate=True)
        num = n+_ln(x,prec)/__ln10_cfm(prec)
    return num.createNewNumber(prec,is_accurate=False)

# __lg2(prec) returns the 10 based logarithm of denary 2, correct
# to the given precision
def __lg2(prec=36):
    num=__ln2(prec)/__ln10_cfm(prec)
    return num

# __lg(x,prec) returns the 10 based logarithm of denary number x, correct
# to the given precision
def __lg(x=None,prec=36):
    if x==1:return upn.Number('0',base=10,prec=prec,is_accurate=True)
    if x==10:return upn.Number('1',base=10,prec=prec,is_accurate=True)
    x=upn.Number(str(x),base=10,prec=prec)
    # A large number is reduced to smaller one
    # x=10^n*a; lg(x)=n + lg(a)
    n=0
    if x>10:
        while(x>=10):
            x=x/10
            n=n+1
        if x==1:return upn.Number(str(n),base=10,prec=prec,is_accurate=True)
    elif x<1 and x>0:
        while(x<1):
            x=x*10
            n=n-1
        if x==1:return upn.Number(str(n),base=10,prec=prec,is_accurate=True)
    return n+_ln(x,prec)/__ln10_cfm(prec)


# ----------------------------- end of lg() -----------------------------------

# --------------------------- start of log(x,base) ----------------------------
# log(x,base,prec) returns the logarithm of the number x of the
# given base, correct to the given precision
# >>> smf.log(upn.Number('1101.11',2),upn.Number('10'))
# b10:1.138302698166281455108983287069545161
# >>> smf.log(upn.Number('1101.11',2),10)
# b10:1.138302698166281455108983287069545161
# >>> smf.log(13.75,upn.Number('10'))
# b10:1.138302698166281455108983287069545161
# b10:1.13830269816628145510898328706954516140213238
# b10:1.13830269816628149241477200048473182
def log(x=None,base=10,prec=36):
    if x==None:raise ValueError("Invalid arguement of ln(x,prec).")
    if dataType(prec)!='int' or prec<2: prec=36
    result=__log(x,base,prec)
    return result.createNewNumber(prec,result.isAccurate())

def __log(x=None,base=10,prec=36):
    if dataType(x) in ['int','float']:
        x=upn.Number(str(x),10,prec,True)
    elif dataType(x)==str(upn.__name__)+'.Number':pass
    else:raise SyntaxError('Invlid argument of function of log(x,base,prec).')

    if dataType(base) in ['int','float']:
        base=upn.Number(str(base),10,prec,True)
    elif dataType(base)==str(upn.__name__)+'.Number':pass
    else:raise SyntaxError('Invlid base of function of log(x,base,prec).')

    if base<0 or x<0: return upn.Number('<undefined>',10,0,True)
    elif base==0 and x==0: return upn.Number('<undefined>',10,0,True)
    elif base==0: return upn.Number('0',10,prec,True)
    elif base!=1 and x==1: return upn.Number('0',10,prec,True)
    elif base==1 and x==1: return upn.Number('<undefined>',10,0,True)
    elif (base>0 and base<1) and x==0:return upn.Number('<inf>',10,0,True)
    elif base>1 and x==0:return upn.Number('<-inf>',10,0,True)
    elif base==x:return upn.Number('1',10,1,True)

    return _ln(x,prec)/_ln(base,prec)


# -------------------------- exponential  functions -----------------------------
# exp(x,prec) returns the exponential value of e**x where x is a denary number
# correct to the given precision value by continued fraction method (CFM)
# >>> smf.exp(1,prec=36)
# b10:2.718281828459045235360287471352662497
# >>> smf.exp(upn.Number('70.5',8),prec=50)
# b10:3907734397750999784942589.28849210618164655946730724460005396323833427408778
# >>> smf.exp(upn.Number('-11011.1101',2),prec=50)
# b10:8.34035856559093677493103790783319787620324928140303e-13
def exp(x=None,prec=36):
    if dataType(prec)!='int' or prec<1: prec=36
    if dataType(x) not in ['int','float',str(upn.__name__)+".Number"]:
        raise ValueError("Invalid argument in function exp(x,prec)")

    if x==0: return upn.Number('1',10,prec=prec,is_accurate=True)
    elif x==1: return __exp(1,prec).createNewNumber(prec,is_accurate=False)
    elif x==-1: return (1/__getE(prec=prec)).createNewNumber(prec,is_accurate=False)

    if dataType(x) in ['int','float']:
        return __exp(x,prec).createNewNumber(prec,is_accurate=False)
    elif dataType(x)==str(upn.__name__)+".Number":
        return _exp(x,prec).createNewNumber(prec,is_accurate=False)


# _exp(x,prec) returns the exponential value of e**x where x is a universal
# precision number object correct to the given precision value 
# by continued fraction method (CFM)
# >>> smf._exp(upn.Number('1'),prec=36)
# b10:2.718281828459045235360287471352662497758
def _exp(x=None,prec=36):
    if x==0: return upn.Number('1',10,prec=prec,is_accurate=True)
    elif x==1: return __exp(1,prec)
    elif x==-1: return 1/__getE(prec)

    delP=upn.Number('1p-'+str(prec),10,prec=prec);

    if prec<=36: prec2=prec+6
    elif prec>36:prec2=int(1.2*prec)
    
    x0=x.copy(); m=1 # m=multiplier
    if x>0 and x<1:pass
    elif x>1:
        # reducing x by considering x=r+kln2; e^x=e^r*2^k
        tmp=x/0.69314718; k=int(tmp.getNormalizedPart()['ipart']);
        x = x - k*__ln2(prec=prec2);
        for i in range(k):m=2*m
    elif x<-1: # e^-x = 1/e^x
        x=-1*x
        # reducing x by considering x=r+kln2; e^x=e^r*2^k
        tmp=x/0.69314718; k=int(tmp.getNormalizedPart()['ipart']);
        x = x - k*__ln2(prec=prec2);
        for i in range(k):m=2*m

    # private function
    def denoFunc(x,y,i,prec):
        t1=upn.Number(str((2+4*i)*y),base=10,prec=prec2)
        t2=upn.Number(str((6+4*i)*y),base=10,prec=prec2)
        return t1+x*x/t2

    # converting x to x/y; where y=1
    i=prec2//4;
    while True:
        deno=denoFunc(x,1,i,prec2)
        for j in range(i,0,-1):
            deno=upn.Number(str(2+4*j),base=10,prec=prec2,is_accurate=False)+x*x/deno
        num1=1+(2*x/(2-x+(x*x/deno)))
        i=i+1
        deno=denoFunc(x,1,i,prec2)
        for j in range(i,0,-1):
            deno=upn.Number(str(2+4*j),base=10,prec=prec2,is_accurate=False)+x*x/deno
        num2=1+(2*x/(2-x+(x*x/deno)))
        if num2==num1:break
        elif num2>num1 and num2-num1 < delP:break
        elif num1>num2 and num1-num2 < delP:break
        i=i+prec2//4;

    if x0>-1 and x0<1:return num2
    elif x0>1:return num2*m
    elif x0<-1:
        num2=num2*m
        #num2.setPrecision(len(str(num2)[4:]))
        return 1/num2


# __exp(x,prec) returns the exponential value of e**x where x is a denary number
# correct to the given precision value by continued fraction method (CFM)
# >>> smf.__exp(1,prec=36)
# b10:2.718281828459045235360287471352662497
def __exp(x=None,prec=36):
    if x==0: return upn.Number('1',10,prec=prec,is_accurate=True)
    elif x==1: return __getE(prec=prec)
    elif x==-1: return 1/__getE(prec=prec)

    delP=upn.Number('1p-'+str(prec),10,prec=prec);

    if prec<=36: prec2=prec+6
    elif prec>36:prec2=int(1.2*prec)
    
    x0=x; m=1 # m=multiplier
    if x>-1 and x<1:
        x=upn.Number(str(x),10,prec=prec2,is_accurate=False);       
    elif x>1:
        # reducing x by considering x=r+kln2; e^x=e^r*2^k
        k=int(x/0.69314718); x = upn.Number(str(x),10,prec=prec2) - k*__ln2(prec=prec2);
        for i in range(k):m=2*m
    elif x<-1: # e^-x = 1/e^x
        x=-1*x
        # reducing x by considering x=r+kln2; e^x=e^r*2^k
        k=int(x/0.69314718); x = upn.Number(str(x),10,prec=prec2) - k*__ln2(prec=prec2);
        for i in range(k):m=2*m


    # private function
    def denoFunc(x,y,i,prec):
        t1=upn.Number(str((2+4*i)*y),base=10,prec=prec2)
        t2=upn.Number(str((6+4*i)*y),base=10,prec=prec2)
        return t1+x*x/t2

    # converting x to x/y; where y=1
    i=prec2//4;
    while True:
        deno=denoFunc(x,1,i,prec2)
        for j in range(i,0,-1):
            deno=upn.Number(str(2+4*j),base=10,prec=prec2,is_accurate=False)+x*x/deno
        num1=1+(2*x/(2-x+(x*x/deno)))
        i=i+1
        deno=denoFunc(x,1,i,prec2)
        for j in range(i,0,-1):
            deno=upn.Number(str(2+4*j),base=10,prec=prec2,is_accurate=False)+x*x/deno
        num2=1+(2*x/(2-x+(x*x/deno)))
        if num2==num1:break
        elif num2>num1 and num2-num1 < delP:break
        elif num1>num2 and num1-num2 < delP:break
        i=i+prec2//4;

    if x0>-1 and x0<1:return num2
    elif x0>1:return num2*m
    elif x0<-1:
        num2=num2*m
        return 1/num2

# __exp2(x,prec) returns the value of e^x where x a denary or UPN
# number and where -1<x<1
# less efficient than exp(x,prec)
# e^x=1+x/1!+x^2/2!+x^3/3!+...
def __exp2(x,prec=36):
    if dataType(prec)!='int' and prec<1: prec=36
    delP=upn.Number('1p-'+str(prec),10,prec=prec);
    if prec<25: prec2=prec+4
    else:prec2=int(1.1*prec)
    SUM=upn.Number('1',10,prec=prec2,is_accurate=False);
    if dataType(x) in ['int','float']:
        t1=upn.Number(1,10,prec=prec2,is_accurate=False);
    elif dataType(x)==str(upn.__name__)+".Number":
        t1=x.copy()
    c=upn.Number(1,10,prec=prec2,is_accurate=False)	# t=term, c=counter   
    while(True):
        t2=t1*(x/c);SUM=SUM+t2
        if t1==t2:break
        elif t1>t2 and t1-t2<delP:break
        elif t1<t2 and t2-t1<delP:break
        t1=t2;c=c+1;t1=t1.createNewNumber(prec=prec2*2,is_accurate=False)
    print(c)
    return SUM

# __getE(prec) returns the exponential value of e='exp(1)'
# e=1+1/1!+1/2!+1/3!+...
def __getE(prec=36):
    if dataType(prec)!='int' and prec<1: prec=36
    delP=upn.Number('1p-'+str(prec),10,prec=prec);
    if prec<25: prec2=prec+4
    else:prec2=int(1.1*prec)
    SUM=upn.Number('2',10,prec=prec2,is_accurate=False);
    t1=upn.Number('1',10,prec=prec2);
    c=upn.Number('1',10,prec=prec2);	# t=term, c=counter   
    i=0 
    while(True):
        t2=t1/(c+1);SUM=SUM+t2
        if t1-t2<delP:break
        t1=t2;c=c+1;
        i=i+1
    return SUM

# ---------------------- end of exponential functions --------------------------

# ------------------------- square root estimations ----------------------------
# calculating sqrt(2) by combined fraction method
# >>> smf.__sqrt2(prec=100)
# b10:1.41421356237309504880168872420969807856967187537694807317667973799073247
# 846210703885038753432764157273501384623
# >>> u.execTime(smf.__sqrt2,prec=100)
# '0.5721414089202881 s'
# >>> 
def __sqrt2_cfm(prec=36):
    delP=upn.Number('1p-'+str(prec),10,prec=prec);

    if prec<=36: prec2=prec+4
    elif prec>36:prec2=int(1.1*prec)

    i=prec2;
    while True:
        deno=upn.Number('2',base=10,prec=prec2)
        for j in range(i,0,-1):
            deno=2+(1/deno)
        num1=1+(1/deno)
        i=i+1
        deno=upn.Number('2',base=10,prec=prec2)
        for j in range(i,0,-1):
            deno=2+(1/deno)
        num2=1+(1/deno)
        if num2==num1:break
        elif num2>num1 and num2-num1 < delP:break
        elif num1>num2 and num1-num2 < delP:break
        i=i+prec2;
    return num2 

# calculating sqrt(2) by bakhshali iterative method
# >>> smf.sqrt2(prec=100)
# b10:1.41421356237309504880168872420969807856967187537694807317667973799073247
# 84621070388503875343276415727
# >>> u.execTime(smf.__sqrt2,prec=100)
# '0.09595537185668945 s'
# >>> 
def sqrt2(prec=36):
    if dataType(prec)!='int' or prec<1: prec=36
    return __sqrt2(prec).createNewNumber(prec,is_accurate=False)

def __sqrt2(prec=36):
    delP=upn.Number('1p-'+str(prec),10,prec=prec);

    if prec<=36: prec2=prec+4
    elif prec>36:prec2=int(1.1*prec)

    x=upn.Number('2',base=10,prec=prec2,is_accurate=False)
    xn1=upn.Number('1',base=10,prec=prec2,is_accurate=False)

    while True:
        an=x/(2*xn1)-xn1/2
        bn=xn1+an
        xn2=bn-an*an/(2*bn)

        if xn1==xn2:break
        elif xn2>xn1 and xn2-xn1 < delP:break
        elif xn1>xn2 and xn1-xn2 < delP:break
        xn1=xn2

    return xn2.createNewNumber(prec*2,is_accurate=False)

       
# calculating sqrt(10) by bakhshali iterative method
# >>> smf.sqrt10(prec=100)
# b10:3.16227766016837933199889354443271853371955513932521682685750485
# 27925944386392382213442481083793002951
# >>> u.execTime(smf.__sqrt2,prec=100)
# '0.09854483604431152 s'
# >>>
def sqrt10(prec=36):
    if dataType(prec)!='int' or prec<1: prec=36
    return __sqrt10(prec).createNewNumber(prec,is_accurate=False)

def __sqrt10(prec=36):
    delP=upn.Number('1p-'+str(prec),10,prec=prec);
    if prec<=36: prec2=prec+4
    elif prec>36:prec2=int(1.1*prec)

    x=upn.Number('10',base=10,prec=prec2,is_accurate=False)
    xn1=upn.Number('3',base=10,prec=prec2,is_accurate=False)

    while True:
        an=x/(2*xn1)-xn1/2
        bn=xn1+an
        xn2=bn-an*an/(2*bn)

        if xn1==xn2:break
        elif xn2>xn1 and xn2-xn1 < delP:break
        elif xn1>xn2 and xn1-xn2 < delP:break
        xn1=xn2
    return xn2.createNewNumber(prec*2,is_accurate=False)


# calculating sqrt(x,prec) by bakhshali iterative method
# >>> smf.sqrt(upn.Number('0.000000abc',16),prec=50)
# b10:1.99971655610369213056965151516651401413531400138775e-4
# >>> u.execTime(smf.__sqrt2,prec=100)
# '0.061365365982055664 s'
# >>> smf.sqrt(upn.Number('10'),prec=100)
# b10:3.16227766016837933199889354443271853371955513932521682685750485
# 27925944386392382213442481083793002951
# >>> u.execTime(smf.sqrt,x=upn.Number('10'),prec=100)
# '0.09975433349609375 s'
# >>>
def sqrt(x=None,prec=36):
    if dataType(prec)!='int' or prec<1: prec=36
    if dataType(x) not in ['int','float',str(upn.__name__)+".Number"]:
        raise ValueError("Invalid argument in function sqrt(x,prec)")
    result=__sqrt(x,prec)
    return result.createNewNumber(prec,result.isAccurate())

def __sqrt(x=None,prec=36):
    if dataType(x) in ['int','float']:
        x=upn.Number(str(x),base=10,prec=prec,is_accurate=True)
    elif dataType(x)==str(upn.__name__)+".Number":pass
    else: raise ValueError("Invalid number of sqrt(x,prec)")  

    if x<0: return upn.Number('<undefined>',10,0,is_accurate=True)
    elif x==2:return upn.Number(str(__sqrt2(prec))[4:],10,prec).createNewNumber(prec*2,False)
    elif x==10:return upn.Number(str(__sqrt10(prec))[4:],10,prec).createNewNumber(prec*2,False)

    l=[0,1,4,9,16,25,36,49,64,81,100,0.01,0.04,0.09,0.16,0.25,0.36,0.49,0.64,0.81]
    root=[0,1,2,3,4,5,6,7,8,9,10,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
    for i in range(len(l)):
        if x==l[i]:return upn.Number(str(root[i]),10,prec,is_accurate=True)

    # private function
    def rootFunc(x,xn1):
        while True:
            an=x/(2*xn1)-xn1/2
            bn=xn1+an
            xn2=bn-an*an/(2*bn)  
            if xn1==xn2:break
            elif xn2>xn1 and xn2-xn1 < delP:break
            elif xn1>xn2 and xn1-xn2 < delP:break
            xn1=xn2
        return xn2

    delP=upn.Number('1p-'+str(prec),10,prec=prec);
    if prec<=36: prec2=prec+4
    elif prec>36:prec2=int(1.1*prec)

    if x>1:
        n=0;m=1
        # reducing the number x0 = x * 10^n            
        if x>100:
            while x>=100:                
                x=x/100;n=n+2;m=10*m	# x>=1, x<100
                if x==1:return upn.Number(str(m),base=10,is_accurate=True)

        #x=upn.Number(str(x),base=10,prec=prec2)
        if x<=4: xn2=rootFunc(x,upn.Number('2',base=10,prec=prec2));
        elif x<=9: xn2=rootFunc(x,upn.Number('3',base=10,prec=prec2))
        elif x<=16: xn2=rootFunc(x,upn.Number('4',base=10,prec=prec2))
        elif x<=25: xn2=rootFunc(x,upn.Number('5',base=10,prec=prec2))
        elif x<=36: xn2=rootFunc(x,upn.Number('6',base=10,prec=prec2))
        elif x<=49: xn2=rootFunc(x,upn.Number('7',base=10,prec=prec2))
        elif x<=64: xn2=rootFunc(x,upn.Number('8',base=10,prec=prec2))
        elif x<=81: xn2=rootFunc(x,upn.Number('9',base=10,prec=prec2))
        elif x<100: xn2=rootFunc(x,upn.Number('9',base=10,prec=prec2))
        xn2=xn2*m;
        if xn2.isInteger():return xn2.createNewNumber(prec*2,is_accurate=True)            
        else: return xn2.createNewNumber(prec*2,is_accurate=False)

    elif x<1:
        n=0;m=1
        if x<=0.01:
            while x<=0.01:
                x=x*100;n=n-2;m=10*m	# x>0.01, x<=1
                if x==1:
                    num=1/upn.Number(str(m),base=10,prec=prec2)
                    return upn.Number(str(num)[4:],base=10,is_accurate=True)
           
        if x>=0.81: xn2=rootFunc(x,upn.Number('0.9',base=10,prec=prec2))
        elif x>=0.64: xn2=rootFunc(x,upn.Number('0.8',base=10,prec=prec2))
        elif x>=0.49: xn2=rootFunc(x,upn.Number('0.7',base=10,prec=prec2))
        elif x>=0.36: xn2=rootFunc(x,upn.Number('0.6',base=10,prec=prec2))
        elif x>=0.25: xn2=rootFunc(x,upn.Number('0.5',base=10,prec=prec2))
        elif x>=0.16: xn2=rootFunc(x,upn.Number('0.4',base=10,prec=prec2))
        elif x>=0.09: xn2=rootFunc(x,upn.Number('0.3',base=10,prec=prec2))
        elif x>=0.04: xn2=rootFunc(x,upn.Number('0.2',base=10,prec=prec2))
        elif x>0: xn2=rootFunc(x,upn.Number('0.1',base=10,prec=prec2))

        if m>100:
            num=xn2/m
            return num.createNewNumber(prec*2,is_accurate=False)
        xn2=xn2/m;        
        return xn2.createNewNumber(prec*2,is_accurate=False)


# ----------------------- end of square root estimations -------------------------
# power(x,y,prec) calculates x^y
# >>> smf.power(3.75,28.0147,prec=100)
# b10:12059068330353029.179872340353830768149473837414354549752585538655295
# 87208838847741208062449956193275
def power(x=None,y=None,prec=36):
    if dataType(prec)!='int' or prec<1: prec=36
    if dataType(x) not in ['int','float',str(upn.__name__)+".Number"]:
        raise ValueError("Invalid argument in function power(x,y,prec)")
    if dataType(y) not in ['int','float',str(upn.__name__)+".Number"]:
        raise ValueError("Invalid argument in function power(x,y,prec)")
    result=__power(x,y,prec)
    return result.createNewNumber(prec,result.isAccurate())

def __power(x=None,y=None,prec=36):
    # a^x is not defined if a<0 and y is float
    if x<0 and (dataType(y)=='float' or (dataType(y)==str(upn.__name__)+".Number" and y.isFloat())):
        return upn.Number('<undefined>',10,0,True)
    # handling exceptional cases ('inf','undefined')
    if dataType(x) in ['int','float']:
        if dataType(y)==str(upn.__name__)+".Number":
            if y.getIntegerPart()=='<UNDEFINED>':return upn.Number('<undefined>',10,0,True)
            elif y.getIntegerPart()=='<INF>' and y.getSign()=='+':
                return upn.Number('<inf>',10,1,True)
            elif y.getIntegerPart()=='<INF>' and y.getSign()=='-':
                return upn.Number('0',10,1,True)
            elif y==0: return upn.Number('1',10,1,True)
    elif dataType(x)==str(upn.__name__)+".Number":
        if x.getIntegerPart()=='<UNDEFINED>':
            return upn.Number('<undefined>',10,0,True)
        elif dataType(y)==str(upn.__name__)+".Number" and y.getIntegerPart()=='<UNDEFINED>':
            return upn.Number('<undefined>',10,0,True)
        if x.getIntegerPart()=='<INF>' and x.getSign()=='+':
            if dataType(y) in ['int','float',str(upn.__name__)+".Number"]:
                if y==0:return upn.Number('<undefined>',10,0,True)
                elif y>0:return upn.Number('<inf>',10,1,True)
                elif y<0:return upn.Number('0',10,1,True)
        elif x.getIntegerPart()=='<INF>' and x.getSign()=='-':
            if dataType(y) in ['int','float',str(upn.__name__)+".Number"]:
                if y==0:return upn.Number('<undefined>',10,0,True)
                elif y>0:return upn.Number('<-inf>',10,1,True)
                elif y<0:return upn.Number('0',10,1,True)

    # handling 0, 1 cases
    if x==1: return upn.Number('1',10,prec,True)            
    elif x==0 and y==0: return upn.Number('<undefined>',10,0,True)
    elif x==0: return upn.Number('0',10,prec,True)
    elif y==0: return upn.Number('1',10,prec,True)
    elif y==1:
        if dataType(x) in ['int','float']:
            return upn.Number(str(x),10,prec,True)
        elif dataType(x)==str(upn.__name__)+".Number":return x

    # a^b=a*a*a*...; a^3=a*a*a
    def a_pow_b_int_int(a,b):
        if b==1: return upn.Number(str(a),10,prec,True)
        prod=1;sign=''
        if a>0 and b>0:
            for i in range(b):prod=prod*a
            return upn.Number(str(prod),10,prec,True)
        elif a<0 and b>0:
            for i in range(b):prod=prod*(-a)            
            if b%2==1:
                return upn.Number(str(-prod),10,prec,True)
            elif b%2==0:
                return upn.Number(str(prod),10,prec,True)
        elif a>0 and b<0:
            a=upn.Number(str(a),10,prec,True)
            for i in range(-1*b):prod=prod*a
            return upn.Number(str(1/prod)[4:],10,prec,True)
        elif a<0 and b<0:
            a=upn.Number(str(a),10,prec,True)
            for i in range(-1*b):prod=prod*a            
            if b%2==1:
                return upn.Number(str(1/prod)[4:],10,prec,True)
            elif b%2==0:
                return upn.Number(str(1/prod)[4:],10,prec,True)

    # a^b=a*a*a*...; a^3=a*a*a
    def a_pow_b_float_int(a,b):
        if prec<=36: prec2=prec+6
        elif prec>36:prec2=int(1.2*prec)
        if b==1: return upn.Number(str(a),10,prec,True)
        prod=upn.Number('1',10,prec2,True);sign=''
        if a>0 and b>0:
            if dataType(x)==str(upn.__name__)+".Number":pass
            elif dataType(x) in ['int','float']:a=upn.Number(str(a),10,prec2,True)
            for i in range(b):prod=prod*a
            return upn.Number(str(prod)[4:],10,prec,True)
        elif a<0 and b>0:
            if dataType(x)==str(upn.__name__)+".Number":pass
            elif dataType(x) in ['int','float']:a=upn.Number(str(a),10,prec2,True)
            for i in range(b):prod=prod*a
            return upn.Number(str(prod)[4:],10,prec,True)
        elif a>0 and b<0:
            if dataType(x)==str(upn.__name__)+".Number":pass
            elif dataType(x) in ['int','float']:a=upn.Number(str(a),10,prec2,True)
            for i in range(-1*b):prod=prod*a
            return upn.Number(str(1/prod)[4:],10,prec,False)
        elif a<0 and b<0:
            if dataType(x)==str(upn.__name__)+".Number":pass
            elif dataType(x) in ['int','float']:a=upn.Number(str(a),10,prec2,True)
            for i in range(-1*b):prod=prod*a            
            if b%2==1:
                return upn.Number(str(1/prod)[4:],10,prec,False)
            elif b%2==0:
                return upn.Number(str(1/prod)[4:],10,prec,False)

    # a^b=a*a*a*...; a^3=a*a*a 
    # integer vs integer
    if dataType(x)=='int' and dataType(y)=='int':
        return a_pow_b_int_int(x,y)
    elif dataType(x)==str(upn.__name__)+".Number" and dataType(y)==str(upn.__name__)+".Number" \
        and x.isInteger() and y.isInteger():
        if x.getBase()==10:a=int(x.getNormalizedPart()['ipart'])
        elif x.getBase() in [2,8,16,32,64]:a=int(x.getBase10Part()['ipart'])
        if y.getBase()==10:b=int(y.getNormalizedPart()['ipart'])
        elif y.getBase() in [2,8,16,32,64]:b=int(y.getBase10Part()['ipart'])
        return a_pow_b_int_int(a,b)
    elif dataType(x)==str(upn.__name__)+".Number" and dataType(y)=='int' \
        and x.isInteger():
        if x.getBase()==10:a=int(x.getNormalizedPart()['ipart'])
        elif x.getBase() in [2,8,16,32,64]:a=int(x.getBase10Part()['ipart'])
        return a_pow_b_int_int(a,y)
    elif dataType(x)==str(upn.__name__)+".Number" and x.isInteger() and dataType(y)=='float' \
        and y==int(y):
        if x.getBase()==10:a=int(x.getNormalizedPart()['ipart'])
        elif x.getBase() in [2,8,16,32,64]:a=int(x.getBase10Part()['ipart'])
        y=int(y)
        return a_pow_b_int_int(a,y)
    elif dataType(x)=='int' and dataType(y)==str(upn.__name__)+".Number" \
        and y.isInteger():
        if y.getBase()==10:b=int(y.getNormalizedPart()['ipart'])
        elif y.getBase() in [2,8,16,32,64]:b=int(y.getBase10Part()['ipart'])
        return a_pow_b_int_int(x,b)
    elif dataType(x)=='float' and x==int(x) and dataType(y)==str(upn.__name__)+".Number" \
        and y.isInteger():
        if y.getBase()==10:b=int(y.getNormalizedPart()['ipart'])
        elif y.getBase() in [2,8,16,32,64]:b=int(y.getBase10Part()['ipart'])
        x=int(x)
        return a_pow_b_int_int(x,b)
    elif dataType(x)=='int' and dataType(y)=='float' and y==int(y): # 5^3.0
        y=int(y); return a_pow_b_int_int(x,y)
    elif dataType(x)=='float' and x==int(x) and dataType(y)=='int': # 5.0^3
        x=int(x); return a_pow_b_int_int(x,y)
    elif dataType(x)=='float' and x==int(x) and dataType(y)=='float' and y==int(y): # 5.0^3.0
        x=int(x); y=int(y); return a_pow_b_int_int(x,y)

    # float vs integer
    elif dataType(x)=='float' and dataType(y)=='int':
        return a_pow_b_float_int(x,y)
    elif dataType(x)=='float' and dataType(y)==str(upn.__name__)+".Number" and y.isInteger():
        if y.getBase()==10:b=int(y.getNormalizedPart()['ipart'])
        elif y.getBase() in [2,8,16,32,64]:b=int(y.getBase10Part()['ipart'])
        if y.isNegative(): return a_pow_b_float_int(x,-1*b)
        return a_pow_b_float_int(x,b)
    elif dataType(x)==str(upn.__name__)+".Number" and dataType(y)=='int':
        return a_pow_b_float_int(x,y)
    elif dataType(x)==str(upn.__name__)+".Number" and dataType(y)==str(upn.__name__)+".Number" and y.isInteger():
        if y.getBase()==10:b=int(y.getNormalizedPart()['ipart'])
        elif y.getBase() in [2,8,16,32,64]:b=int(y.getBase10Part()['ipart'])
        if y.isNegative(): return a_pow_b_float_int(x,-1*b)
        return a_pow_b_float_int(x,b)
    elif dataType(x)=='float' and dataType(y)=='float' and y==int(y): # 5.4^3.0
        y=int(y); return a_pow_b_float_int(x,y)

    # x^y=?; y=m.n; x^(m.n)=x^(m+.n)=x^m*x^(.n)=x^m*e^(.n*ln(x))
    elif dataType(y)=='float':
        if x<0:return upn.Number('<undefined>',10,0,True)

        if prec<=36: prec2=prec+4
        elif prec>36:prec2=int(1.1*prec)

        if y==1.0: return upn.Number(str(x),10,prec,True)
        y=upn.Number(str(y),10,prec=prec2)
        if y.getBase()==10:
            m=int(y.getNormalizedPart()['ipart'])
        elif y.getBase() in [2,8,16,32,64]:
            m=int(y.getBase10Part()['ipart'])
        if y.isPositive():n=y-m
        elif y.isNegative():n=-y-m
        
        if dataType(x) in ['int','float'] and x>0:
            tmp=exp(n*__ln(x,prec=prec2),prec=prec2)
            prod=upn.Number('1',10,prec=prec2)
            for i in range(m):prod=prod*x
            prod=tmp*prod
            if y>0: return prod.createNewNumber(prec*2,is_accurate=False)
            elif y<0: return (1/prod).createNewNumber(prec*2,is_accurate=False)
        elif dataType(x)==str(upn.__name__)+".Number":
            tmp=exp(n*ln(x,prec=prec2),prec=prec2)
            prod=1
            for i in range(m):prod=x*prod
            prod=tmp*prod
            if y>0: return prod.createNewNumber(prec*2,is_accurate=False)
            elif y<0: return (1/prod).createNewNumber(prec*2,is_accurate=False)

    # power is a float
    # x^y=?; y=m.n; x^(m.n)=x^(m+.n)=x^m*x^(.n)=x^m*e^(.n*ln(x))
    elif dataType(y)==str(upn.__name__)+".Number" and y.isFloat():
        if x<0:return upn.Number('<undefined>',10,0,True)

        if prec<=36: prec2=prec+4
        elif prec>36:prec2=int(1.1*prec)

        if y.getBase()==10:
            m=int(y.getNormalizedPart()['ipart'])
        elif y.getBase() in [2,8,16,32,64]:
            m=int(y.getBase10Part()['ipart'])

        if y.isPositive():n=y-m
        elif y.isNegative():n=-y-m
        if dataType(x) in ['int','float'] and x>0:
            tmp=_exp(n*__ln(x,prec=prec2),prec=prec2)
            prod=upn.Number('1',10,prec=prec2)
            for i in range(m):prod=prod*x
            prod=tmp*prod
            if y>0: return prod.createNewNumber(prec*2,is_accurate=False)
            elif y<0: return (1/prod).createNewNumber(prec*2,is_accurate=False)
        elif dataType(x)==str(upn.__name__)+".Number":
            tmp=_exp(n*_ln(x,prec=prec2),prec=prec2)
            prod=1
            for i in range(m):prod=x*prod
            prod=tmp*prod
            if y>0: return prod.createNewNumber(prec*2,is_accurate=False)
            elif y<0: return (1/prod).createNewNumber(prec*2,is_accurate=False)


# ---------------------- trigonometric function estimations ------------------------
# sin(x,unit,prec) returns sine of x where x is in degree by default
# It can handle radian too. |x|<pi/2 or 2*|x|<pi
# unit='d','D' for degree, 'r','R','c' for radian
# Domain: {R}	Range: -1<=f(x)<=1
# >>> smf.sin(upn.Number('-200'),prec=50)
# b10:0.34202014332566873304409961468225958076308336751417
# >>> smf.sin(upn.Number('-900'),prec=50)
# b10:0
# >>> smf.sin(upn.Number('450'),prec=50)
# b10:1
def sin(x=None,unit='d',prec=36):
    if x==None:raise ValueError('Argument of sin() missing')
    if dataType(x) not in ['int','float',str(upn.__name__)+".Number"]:
        raise ValueError("Invalid argument in function sin(x,unit,prec)")
    if unit not in ['d','D','degre','Degre','r','R','c','rad','Rad','radian','Radian']:
        raise Exception('Unit Error.')
    if dataType(prec)!='int' or prec<1: prec=36
    result=__sin(x,unit,prec)
    return result.createNewNumber(prec,result.isAccurate())

# __sin(x,unit,prec) calculates sin(x) where x is a denary angle
# default unit is degree
def __sin(x=None,unit='d',prec=36):
    if dataType(x) in ['int','float']:
        x=upn.Number(str(x),base=10,prec=prec,is_accurate=True)
    elif dataType(x)==str(upn.__name__)+".Number":pass
    else: raise ValueError("Invalid number of sin(x,unit,prec)") 

    delP=upn.Number('1p-'+str(prec),10,prec=prec);
    if prec<=36: prec2=prec+8
    elif prec>36:prec2=int(1.2*prec)

    neg=0				# neg=negative sign, 1 for true
    if x<0:
        neg=1
        x=-1*x
    
    PI=pi.getPI(prec2)
    x1,x2=PI/2,PI/180  
  
    if unit in ['d','D','degre','Degre']:
        if neg==0:
            if x%30==0 and (x//30)%12 in [0,6]:
                return upn.Number('0',base=10,prec=prec,is_accurate=True)
            elif x%30==0 and (x//30)%12 in [1,5]: 
                return upn.Number('0.5',base=10,prec=prec,is_accurate=True)
            elif x%30==0 and (x//30)%12 in [7,11]:
                return upn.Number('-0.5',base=10,prec=prec,is_accurate=True)
            elif x%30==0 and (x//30)%12==3:
                return upn.Number('1',base=10,prec=prec,is_accurate=True)
            elif x%30==0 and (x//30)%12==9:
                return upn.Number('-1',base=10,prec=prec,is_accurate=True)
        elif neg==1:
            if x%30==0 and (x//30)%12 in [0,6]:
                return upn.Number('0',base=10,prec=prec,is_accurate=True)
            elif x%30==0 and (x//30)%12 in [1,5]: 
                return upn.Number('-0.5',base=10,prec=prec,is_accurate=True)
            elif x%30==0 and (x//30)%12 in [7,11]:
                return upn.Number('0.5',base=10,prec=prec,is_accurate=True)
            elif x%30==0 and (x//30)%12==3:
                return upn.Number('-1',base=10,prec=prec,is_accurate=True)
            elif x%30==0 and (x//30)%12==9:
                return upn.Number('1',base=10,prec=prec,is_accurate=True)
        x=x*x2		# degree converted to radian

    # q=quadrant number, 1=First quadrant, 2=Second quadrant
    # 3=Third quadrant, 4=Fourth quadrant    
    q=1+x//x1-4*((x//x1)//4)
    if neg==1:q=5-q
    # find the basic angle in radian
    if neg==0 and q in [2,4]:x=x1-x%x1
    elif neg==1 and q in [1,3]:x=x1-x%x1
    else:x=x%x1  

    if neg==0:  
        if x==0:return upn.Number('0',base=10,prec=prec,is_accurate=True)
        elif x==PI/2:return upn.Number('1',base=10,prec=prec,is_accurate=True)
        elif x==PI/6:return upn.Number('0.5',base=10,prec=prec,is_accurate=True)
    elif neg==1:  
        if x==0:return upn.Number('0',base=10,prec=prec,is_accurate=True)
        elif x==PI/2:return upn.Number('-1',base=10,prec=prec,is_accurate=True)
        elif x==PI/6:return upn.Number('-0.5',base=10,prec=prec,is_accurate=True)

    i=1				# i=counter
    t,s=x.copy(),x.copy()	# initialization of term and sum
    while(True):        
        t=t*(-1)*x*x/(2*i*(2*i+1))
        if t.getPrecision()>3*prec2:
            t=t.createNewNumber(prec2*2,False)
        if t>0 and t<delP: break
        elif t<0 and -1*t<delP: break
        s=s+t
        i=i+1 
    if q in [1,2]: return s.createNewNumber(prec*2,False)
    elif q in [3,4]: return (-1*s).createNewNumber(prec*2,False)


# cos(x,unit,prec) returns cosine of x where x is in degree by default
# It can handle radian too. |x|<pi/2 or 2*|x|<pi
# unit='d','D' for degree, 'r','R','c' for radian
# Domain: {R}	Range: -1<=f(x)<=1
# >>> smf.cos(upn.Number('-200'),prec=50)
# b10:-0.93969262078590838405410927732473146993620813426446
# >>> smf.cos(upn.Number('-900'),prec=50)
# b10:-1
# >>> smf.cos(upn.Number('450'),prec=50)
# b10:0 
def cos(x=None,unit='d',prec=36):
    if x==None:raise ValueError('Argument of cos() missing')
    if dataType(x) not in ['int','float',str(upn.__name__)+".Number"]:
        raise ValueError("Invalid argument in function cos(x,unit,prec)")
    if unit not in ['d','D','degre','Degre','r','R','c','rad','Rad','radian','Radian']:
        raise Exception('Unit Error.')
    if dataType(prec)!='int' or prec<1: prec=36
    result=__cos(x,unit,prec)
    return result.createNewNumber(prec,result.isAccurate())

# __cos(x,unit) returns cosine of x where x is in degree by default
# It can handle radian too. |x|<pi/2 or 2*|x|<pi
# unit='d','D' for degree, 'r','R','c' for radian
# Domain: {R}	Range: -1<=f(x)<=1
def __cos(x=None,unit='d',prec=36):
    if dataType(x) in ['int','float']:
        x=upn.Number(str(x),base=10,prec=prec,is_accurate=True)
    elif dataType(x)==str(upn.__name__)+".Number":pass
    else: raise ValueError("Invalid number of cos(x,unit,prec)") 

    delP=upn.Number('1p-'+str(prec),10,prec=prec);
    if prec<=36: prec2=prec+8
    elif prec>36:prec2=int(1.2*prec)

    neg=0				# neg=negative sign, 1 for true
    if x<0:
        neg=1
        x=-1*x
    
    PI=pi.getPI(prec2)
    x1,x2=PI/2,PI/180  
  
    if unit in ['d','D','degre','Degre']:
        if x%30==0 and (x//30)%12==0:
            return upn.Number('1',base=10,prec=prec,is_accurate=True)
        elif x%30==0 and (x//30)%12==6:
            return upn.Number('-1',base=10,prec=prec,is_accurate=True)
        elif x%30==0 and (x//30)%12 in [2,10]: 
            return upn.Number('0.5',base=10,prec=prec,is_accurate=True)
        elif x%30==0 and (x//30)%12 in [4,8]:
            return upn.Number('-0.5',base=10,prec=prec,is_accurate=True)
        elif x%30==0 and (x//30)%12 in [3,9]:
            return upn.Number('0',base=10,prec=prec,is_accurate=True)
        x=x*x2		# degree converted to radian

    # q=quadrant number, 1=First quadrant, 2=Second quadrant
    # 3=Third quadrant, 4=Fourth quadrant    
    q=1+x//x1-4*((x//x1)//4)
    if neg==1:q=5-q
    # find the basic angle in radian
    if neg==0 and q in [2,4]:x=x1-x%x1
    elif neg==1 and q in [1,3]:x=x1-x%x1
    else:x=x%x1

    if neg==0 and x==0:return upn.Number('1',base=10,prec=prec,is_accurate=True)
    elif neg==1 and x==0:return upn.Number('-1',base=10,prec=prec,is_accurate=True)
    elif x==PI/2:return upn.Number('0',base=10,prec=prec,is_accurate=True)
    elif x==PI/3:return upn.Number('0.5',base=10,prec=prec,is_accurate=True)

    i=1
    t,s=upn.Number('1',10,prec2),upn.Number('1',10,prec2)	# initialization of term and sum
    while(True):        
        t=t*(-1)*x*x/(2*i*(2*i-1))
        if t.getPrecision()>3*prec2:
            t=t.createNewNumber(prec2*2,False)
        if t>0 and t<delP: break
        elif t<0 and -1*t<delP: break
        s=s+t
        i=i+1
    if q in [1,4]: return s.createNewNumber(prec*2,False)
    elif q in [2,3]: return (-1*s).createNewNumber(prec*2,False)


# tan(x,unit,prec) returns tangent of x where x is in degree by default
# It can handle radian too. |x|<pi/2 or 2*|x|<pi
# unit='d','D' for degree, 'r','R','c' for radian
# Domain: {R}	Range: -inf<=f(x)<=inf
# >>> smf.tan(upn.Number('-200'),prec=50)
# b10:-0.93969262078590838405410927732473146993620813426446
# >>> smf.tan(upn.Number('-900'),prec=50)
# b10:-1
# >>> smf.tan(upn.Number('450'),prec=50)
# b10:0 
def tan(x=None,unit='d',prec=36):
    if x==None:raise ValueError('Argument of tan() missing')
    if dataType(x) not in ['int','float',str(upn.__name__)+".Number"]:
        raise ValueError("Invalid argument in function tan(x,unit,prec)")
    if unit not in ['d','D','degre','Degre','r','R','c','rad','Rad','radian','Radian']:
        raise Exception('Unit Error.')
    if dataType(prec)!='int' or prec<1: prec=36
    result=__tan(x,unit,prec)
    return result.createNewNumber(prec,result.isAccurate())

# __tan(x,unit,prec) returns tangent of x where x is in degree by default
# It is the precission version of tan(x)
# unit='d','D' for degree, 'r','R','c' for radian
# Domain: {R}	Range: |f(x)|<=infinity
def __tan(x=None,unit='d',prec=36):
    if dataType(prec)!='int' or prec<1: prec=36

    if prec<=36: prec2=prec+8
    elif prec>36:prec2=int(1.2*prec)

    neg=0				# neg=negative sign, 1 for true
    if x<0:
        neg=1
        x=-1*x
    
    PI=pi.getPI(prec2)
    x1,x2=PI/2,PI/180 

    if unit in ['d','D','degre','Degre']:
        if neg==0:
            if x%45==0 and (x//45)%8 in [0,4]:
                return upn.Number('0',base=10,prec=prec,is_accurate=True)
            elif x%45==0 and (x//45)%8 in [1,5]: 
                return upn.Number('1',base=10,prec=prec,is_accurate=True)
            elif x%45==0 and (x//45)%8 in [3,7]: 
                return upn.Number('-1',base=10,prec=prec,is_accurate=True)
            elif x%45==0 and (x//45)%8==2: 
                return upn.Number('<inf>',base=10,prec=prec,is_accurate=True)
            elif x%45==0 and (x//45)%8==6: 
                return upn.Number('<-inf>',base=10,prec=prec,is_accurate=True)
        elif neg==1:
            if x%45==0 and (x//45)%8 in [0,4]:
                return upn.Number('0',base=10,prec=prec,is_accurate=True)
            elif x%45==0 and (x//45)%8 in [1,5]: 
                return upn.Number('-1',base=10,prec=prec,is_accurate=True)
            elif x%45==0 and (x//45)%8 in [3,7]: 
                return upn.Number('1',base=10,prec=prec,is_accurate=True)
            elif x%45==0 and (x//45)%8==2: 
                return upn.Number('<-inf>',base=10,prec=prec,is_accurate=True)
            elif x%45==0 and (x//45)%8==6: 
                return upn.Number('<inf>',base=10,prec=prec,is_accurate=True)
        x=x*x2		# degree converted to radian

    # q=quadrant number, 1=First quadrant, 2=Second quadrant
    # 3=Third quadrant, 4=Fourth quadrant    
    q=1+x//x1-4*((x//x1)//4)
    if neg==1:q=5-q
    # find the basic angle in radian
    if neg==0 and q in [2,4]:x=x1-x%x1
    elif neg==1 and q in [1,3]:x=x1-x%x1
    else:x=x%x1

    if neg==0:  
        if x==0 or x==PI:return upn.Number('0',base=10,prec=prec,is_accurate=True)
        elif x==PI/4:return upn.Number('1',base=10,prec=prec,is_accurate=True)
        elif x==PI/2:return upn.Number('<inf>',base=10,prec=prec,is_accurate=True)
    elif neg==1:  
        if x==0 or x==PI:return upn.Number('0',base=10,prec=prec,is_accurate=True)
        elif x==PI/4:return upn.Number('-1',base=10,prec=prec,is_accurate=True)
        elif x==PI/2:return upn.Number('<-inf>',base=10,prec=prec,is_accurate=True)

    if q in [1,3]:
        return (__sin(x,unit='r',prec=prec2)/__cos(x,unit='r',prec=prec2)).createNewNumber(prec*2,False)
    elif q in [2,4]:
        return (-1*__sin(x,unit='r',prec=prec2)/__cos(x,unit='r',prec=prec2)).createNewNumber(prec*2,False)



# cot(x,unit) returns cotangent of x where x is in degree by default
# unit='d','D' for degree, 'r','R','c' for radian
# Domain: {R}	Range: |f(x)|<=infinity
def cot(x=None,unit='d',prec=36):
    if x==None:raise ValueError('Argument of cot() missing')
    if dataType(x) not in ['int','float',str(upn.__name__)+".Number"]:
        raise ValueError("Invalid argument in function cot(x,unit,prec)")
    if unit not in ['d','D','degre','Degre','r','R','c','rad','Rad','radian','Radian']:
        raise Exception('Unit Error.')
    if dataType(prec)!='int' or prec<1: prec=36
    result=__cot(x,unit,prec)
    return result.createNewNumber(prec,result.isAccurate())

def __cot(x=None,unit='d',prec=36):
    if prec<=36: prec2=prec+8
    elif prec>36:prec2=int(1.2*prec)

    neg=0				# neg=negative sign, 1 for true
    if x<0:
        neg=1
        x=-1*x
    
    PI=pi.getPI(prec2)
    x1,x2=PI/2,PI/180  

    if unit in ['d','D','degre','Degre']:
        if neg==0:
            if x%45==0 and (x//45)%8==0:
                return upn.Number('<inf>',base=10,prec=prec,is_accurate=True)
            elif x%45==0 and (x//45)%8==4:
                return upn.Number('<-inf>',base=10,prec=prec,is_accurate=True)
            elif x%45==0 and (x//45)%8 in [1,5]: 
                return upn.Number('1',base=10,prec=prec,is_accurate=True)
            elif x%45==0 and (x//45)%8 in [3,7]: 
                return upn.Number('-1',base=10,prec=prec,is_accurate=True)
            elif x%45==0 and (x//45)%8 in [2,6]: 
                return upn.Number('0',base=10,prec=prec,is_accurate=True)
        elif neg==1:
            if x%45==0 and (x//45)%8==0:
                return upn.Number('<-inf>',base=10,prec=prec,is_accurate=True)
            elif x%45==0 and (x//45)%8==4:
                return upn.Number('<inf>',base=10,prec=prec,is_accurate=True)
            elif x%45==0 and (x//45)%8 in [1,5]: 
                return upn.Number('-1',base=10,prec=prec,is_accurate=True)
            elif x%45==0 and (x//45)%8 in [3,7]: 
                return upn.Number('1',base=10,prec=prec,is_accurate=True)
            elif x%45==0 and (x//45)%8 in [2,6]: 
                return upn.Number('0',base=10,prec=prec,is_accurate=True)
        x=x*x2		# degree converted to radian

    # q=quadrant number, 1=First quadrant, 2=Second quadrant
    # 3=Third quadrant, 4=Fourth quadrant    
    q=1+x//x1-4*((x//x1)//4)
    if neg==1:q=5-q
    # find the basic angle in radian
    if neg==0 and q in [2,4]:x=x1-x%x1
    elif neg==1 and q in [1,3]:x=x1-x%x1
    else:x=x%x1

    if neg==0:  
        if x==0:return upn.Number('<inf>',base=10,prec=prec,is_accurate=True)
        if x==PI:return upn.Number('<-inf>',base=10,prec=prec,is_accurate=True)
        elif x==PI/4:return upn.Number('1',base=10,prec=prec,is_accurate=True)
        elif x==PI/2:return upn.Number('0',base=10,prec=prec,is_accurate=True)
    elif neg==1:  
        if x==0:return upn.Number('<-inf>',base=10,prec=prec,is_accurate=True)
        if x==PI:return upn.Number('<inf>',base=10,prec=prec,is_accurate=True)
        elif x==PI/4:return upn.Number('-1',base=10,prec=prec,is_accurate=True)
        elif x==PI/2:return upn.Number('0',base=10,prec=prec,is_accurate=True)

    if q in [1,3]:
        return (__cos(x,unit='r',prec=prec2)/__sin(x,unit='r',prec=prec2)).createNewNumber(prec,False)
    elif q in [2,4]:
        return (-1*__cos(x,unit='r',prec=prec2)/__sin(x,unit='r',prec=prec2)).createNewNumber(prec,False)


# sec(x,unit) returns secant of x where x is in degree by default
# unit='d','D' for degree, 'r','R','c' for radian
# Domain: {R}	Range: 1<|f(x)|<=infinity
def sec(x=None,unit='d',prec=36):
    if x==None:raise ValueError('Argument of sec() missing')
    if dataType(x) not in ['int','float',str(upn.__name__)+".Number"]:
        raise ValueError("Invalid argument in function sec(x,unit,prec)")
    if unit not in ['d','D','degre','Degre','r','R','c','rad','Rad','radian','Radian']:
        raise Exception('Unit Error.')
    if dataType(prec)!='int' or prec<1: prec=36
    result=__sec(x,unit,prec)
    return result.createNewNumber(prec,result.isAccurate())

def __sec(x=None,unit='d',prec=36):
    if prec<=36: prec2=prec+8
    elif prec>36:prec2=int(1.2*prec)

    neg=0				# neg=negative sign, 1 for true
    if x<0:
        neg=1
        x=-1*x
    
    PI=pi.getPI(prec2)
    x1,x2=PI/2,PI/180  
  
    if unit in ['d','D','degre','Degre']:
        if x%30==0 and (x//30)%12==0:
            return upn.Number('1',base=10,prec=prec,is_accurate=True)
        elif x%30==0 and (x//30)%12==6:
            return upn.Number('-1',base=10,prec=prec,is_accurate=True)
        elif x%30==0 and (x//30)%12 in [2,10]: 
            return upn.Number('2',base=10,prec=prec,is_accurate=True)
        elif x%30==0 and (x//30)%12 in [4,8]:
            return upn.Number('-2',base=10,prec=prec,is_accurate=True)
        elif x%30==0 and (x//30)%12 in [3,9]:
            return upn.Number('<inf>',base=10,prec=prec,is_accurate=True)
        x=x*x2		# degree converted to radian

    # q=quadrant number, 1=First quadrant, 2=Second quadrant
    # 3=Third quadrant, 4=Fourth quadrant    
    q=1+x//x1-4*((x//x1)//4)
    if neg==1:q=5-q
    # find the basic angle in radian
    if neg==0 and q in [2,4]:x=x1-x%x1
    elif neg==1 and q in [1,3]:x=x1-x%x1
    else:x=x%x1

    if neg==0 and x==0:return upn.Number('1',base=10,prec=prec,is_accurate=True)
    elif neg==1 and x==0:return upn.Number('-1',base=10,prec=prec,is_accurate=True)
    elif x==PI/2:return upn.Number('<inf>',base=10,prec=prec,is_accurate=True)
    elif x==PI/3:return upn.Number('2',base=10,prec=prec,is_accurate=True)

    if q in [1,4]:
        return (1/__cos(x,unit='r',prec=prec2)).createNewNumber(prec,False)
    elif q in [2,3]:
        return (-1/__cos(x,unit='r',prec=prec2)).createNewNumber(prec,False)


# cosec(x,unit) returns cosecant of x where x is in degree by default
# unit='d','D' for degree, 'r','R','c' for radian
# Domain: {R}	Range: 1<|f(x)|<=infinity
def cosec(x=None,unit='d',prec=36):
    if x==None:raise ValueError('Argument of cosec() missing')
    if dataType(x) not in ['int','float',str(upn.__name__)+".Number"]:
        raise ValueError("Invalid argument in function cosec(x,unit,prec)")
    if unit not in ['d','D','degre','Degre','r','R','c','rad','Rad','radian','Radian']:
        raise Exception('Unit Error.')
    if dataType(prec)!='int' or prec<1: prec=36
    result=__cosec(x,unit,prec)
    return result.createNewNumber(prec,result.isAccurate())

def __cosec(x=None,unit='d',prec=36):
    if prec<=36: prec2=prec+8
    elif prec>36:prec2=int(1.2*prec)

    neg=0				# neg=negative sign, 1 for true
    if x<0:
        neg=1
        x=-1*x
    
    PI=pi.getPI(prec2)
    x1,x2=PI/2,PI/180  
  
    if unit in ['d','D','degre','Degre']:
        if neg==0:
            if x%30==0 and (x//30)%12 in [0,6]:
                return upn.Number('<inf>',base=10,prec=prec,is_accurate=True)
            elif x%30==0 and (x//30)%12 in [1,5]: 
                return upn.Number('2',base=10,prec=prec,is_accurate=True)
            elif x%30==0 and (x//30)%12 in [7,11]:
                return upn.Number('-2',base=10,prec=prec,is_accurate=True)
            elif x%30==0 and (x//30)%12==3:
                return upn.Number('1',base=10,prec=prec,is_accurate=True)
            elif x%30==0 and (x//30)%12==9:
                return upn.Number('-1',base=10,prec=prec,is_accurate=True)
        elif neg==1:
            if x%30==0 and (x//30)%12 in [0,6]:
                return upn.Number('<inf>',base=10,prec=prec,is_accurate=True)
            elif x%30==0 and (x//30)%12 in [1,5]: 
                return upn.Number('-2',base=10,prec=prec,is_accurate=True)
            elif x%30==0 and (x//30)%12 in [7,11]:
                return upn.Number('2',base=10,prec=prec,is_accurate=True)
            elif x%30==0 and (x//30)%12==3:
                return upn.Number('-1',base=10,prec=prec,is_accurate=True)
            elif x%30==0 and (x//30)%12==9:
                return upn.Number('1',base=10,prec=prec,is_accurate=True)
        x=x*x2		# degree converted to radian

    # q=quadrant number, 1=First quadrant, 2=Second quadrant
    # 3=Third quadrant, 4=Fourth quadrant    
    q=1+x//x1-4*((x//x1)//4)
    if neg==1:q=5-q
    # find the basic angle in radian
    if neg==0 and q in [2,4]:x=x1-x%x1
    elif neg==1 and q in [1,3]:x=x1-x%x1
    else:x=x%x1  

    if neg==0:  
        if x==0:return upn.Number('<inf>',base=10,prec=prec,is_accurate=True)
        elif x==PI/2:return upn.Number('-1',base=10,prec=prec,is_accurate=True)
        elif x==PI/6:return upn.Number('2',base=10,prec=prec,is_accurate=True)
    elif neg==1:  
        if x==0:return upn.Number('<inf>',base=10,prec=prec,is_accurate=True)
        elif x==PI/2:return upn.Number('1',base=10,prec=prec,is_accurate=True)
        elif x==PI/6:return upn.Number('-2',base=10,prec=prec,is_accurate=True)

    if q in [1,2]:
        return (1/__sin(x,unit='r',prec=prec2)).createNewNumber(prec*2,False)
    elif q in [3,4]:
        return (-1/__sin(x,unit='r',prec=prec2)).createNewNumber(prec*2,False)


# --------------------------Trigonometric Inverse Functions--------------------------------
# asin(x,unit,prec) returns radian value of inverse of sine of x
# Default output unit is degree
# Domain: -1<=x<=1	Range: -90<=f(x)<=90 or -pi/2<=f(x)<=pi/2
# unit='d','D' for degree, 'r','R','c' for radian
# >>> smf.asin(upn.Number('0.4',10),prec=50)
# b10:23.578178478201831099898328376307220932923234216313
# >>> smf.asin(upn.Number('0'),prec=50)
# b10:0
# >>> smf.asin(upn.Number('1'),prec=50)
# b10:90
def asin(x=None,unit='d',prec=36):
    if x==None:raise ValueError('Argument of asin() missing')
    if dataType(x) not in ['int','float',str(upn.__name__)+".Number"]:
        raise ValueError("Invalid argument in function asin(x,unit,prec)")
    if x<-1 or x>1: raise ValueError("Invalid argument of asin(x). |x|<=1")
    if unit not in ['d','D','degre','Degre','r','R','c','rad','Rad','radian','Radian']:
        raise Exception('Unit Error.') 
    if dataType(prec)!='int' or prec<1: prec=36

    result=__asin(x,unit,prec)
    return result.createNewNumber(prec,result.isAccurate())


# __asin(x,unit,prec) calculates inverse of sin(x) either in degree or in radian
# where x is a denary number between -1 and +1
# Domain: -1<=x<=1	Range: -pi/2<=f(x)<=pi/2
def __asin(x=None,unit='d',prec=36):
    if dataType(x) in ['int','float']:
        x=upn.Number(str(x),base=10,prec=prec,is_accurate=True)
    elif dataType(x)==str(upn.__name__)+".Number":pass
    else: raise ValueError("Invalid number of asin(x,unit,prec)") 

    delP=upn.Number('1p-'+str(prec),10,prec=prec);
    if prec<=36: prec2=prec+6
    elif prec>36:prec2=int(1.15*prec)

    PI=pi.getPI(prec2)

    if unit in ['r','R','c','rad','Rad','radian','Radian']:
        if x==0:return upn.Number('0',base=10,prec=prec,is_accurate=True)
        elif x==0.5:return upn.Number(str(PI/6)[4:],10,prec2).createNewNumber(prec*2,False)
        elif x==1:return upn.Number(str(PI/2)[4:],10,prec2).createNewNumber(prec*2,False)
        elif x==-0.5:return upn.Number(str(-PI/6)[4:],10,prec2).createNewNumber(prec*2,False)
        elif x==-1:return upn.Number(str(-PI/2)[4:],10,prec2).createNewNumber(prec*2,False)
    elif unit in ['d','D','degre','Degre']:
        if x==0:return upn.Number('0',base=10,prec=prec,is_accurate=True)
        elif x==0.5:return upn.Number('30',base=10,prec=prec,is_accurate=True)
        elif x==1:return upn.Number('90',base=10,prec=prec,is_accurate=True)
        elif x==-0.5:return upn.Number('-30',base=10,prec=prec,is_accurate=True)
        elif x==-1:return upn.Number('-90',base=10,prec=prec,is_accurate=True)
                
    i=1				# i=counter
    t,s=x.copy(),x.copy()	# initialization of term and sum
    while(True):        
        t=t*(2*i-1)*(2*i-1)*x*x/(2*i*(2*i+1))
        if t.getPrecision()>3*prec2:
            t=t.createNewNumber(prec2*2,False)
        if t>0 and t<delP: break
        elif t<0 and -1*t<delP: break
        s=s+t
        i=i+1
    if unit in ['r','R','c','rad','Rad','radian','Radian']: 
        return upn.Number(str(s)[4:],10,prec2).createNewNumber(prec*2,False)
    elif unit in ['d','D','degre','Degre']:
        return upn.Number(str(s*180/PI)[4:],10,prec2).createNewNumber(prec*2,False)


# acos(x,unit,prec) returns radian or degree value of inverse of cosine of x
# Default output unit is degree
# Domain: -1<=x<=1	Range: -90<=f(x)<=90 or -pi/2<=f(x)<=pi/2
# unit='d','D' for degree, 'r','R','c' for radian
# >>> smf.acos(upn.Number('0.4',10),prec=50)
# b10:23.578178478201831099898328376307220932923234216313
# >>> smf.acos(upn.Number('0'),prec=50)
# b10:90
# >>> smf.acos(upn.Number('1'),prec=50)
# b10:0
# >>> smf.acos(upn.Number('-1'),prec=50)
# b10:180
def acos(x=None,unit='d',prec=36):
    if x==None:raise ValueError('Argument of acos() missing')
    if dataType(x) not in ['int','float',str(upn.__name__)+".Number"]:
        raise ValueError("Invalid argument in function acos(x,unit,prec)")
    if x<-1 or x>1: raise ValueError("Invalid argument of acos(x). |x|<=1")
    if unit not in ['d','D','degre','Degre','r','R','c','rad','Rad','radian','Radian']:
        raise Exception('Unit Error.') 
    if dataType(prec)!='int' or prec<1: prec=36

    result=__acos(x,unit,prec)
    return result.createNewNumber(prec,result.isAccurate())


# __acos(x,prec) calculates inverse of cosine(x) either in degree or in radian
# where x is a denary number between -1 and +1
# Domain: -1<=x<=1	Range: -90<=f(x)<=90 or -pi/2<=f(x)<=pi/2
def __acos(x=None,unit='d',prec=36):
    if dataType(x) in ['int','float']:
        x=upn.Number(str(x),base=10,prec=prec,is_accurate=True)
    elif dataType(x)==str(upn.__name__)+".Number":pass
    else: raise ValueError("Invalid number of acos(x,unit,prec)") 

    delP=upn.Number('1p-'+str(prec),10,prec=prec);
    if prec<=36: prec2=prec+6
    elif prec>36:prec2=int(1.15*prec)
    PI=pi.getPI(prec2)

    if unit in ['r','R','c','rad','Rad','radian','Radian']:
        if x==0:return upn.Number(str(PI/2)[4:],base=10,prec=prec).createNewNumber(prec*2,False)
        elif x==0.5:return upn.Number(str(PI/3)[4:],base=10,prec=prec).createNewNumber(prec*2,False)
        elif x==1:return upn.Number('0',base=10,prec=prec).createNewNumber(prec*2,False)
        elif x==-0.5:return upn.Number(str(-PI/3)[4:],base=10,prec=prec).createNewNumber(prec*2,False)
        elif x==-1:return upn.Number(str(PI)[4:],base=10,prec=prec).createNewNumber(prec*2,False)
    elif unit in ['d','D','degre','Degre']:
        if x==0:return upn.Number('90',base=10,prec=prec,is_accurate=True)
        elif x==0.5:return upn.Number('60',base=10,prec=prec,is_accurate=True)
        elif x==1:return upn.Number('0',base=10,prec=prec,is_accurate=True)
        elif x==-0.5:return upn.Number('-60',base=10,prec=prec,is_accurate=True)
        elif x==-1:return upn.Number('180',base=10,prec=prec,is_accurate=True)
                
    i=1				# i=counter
    t,s=x.copy(),x.copy()	# initialization of term and sum
    while(True):        
        t=t*(2*i-1)*(2*i-1)*x*x/(2*i*(2*i+1))
        if t.getPrecision()>3*prec2:
            t=t.createNewNumber(prec2*2,False)
        if t>0 and t<delP: break
        elif t<0 and -1*t<delP: break
        s=s+t
        i=i+1
    if unit in ['r','R','c','rad','Rad','radian','Radian']: 
        return upn.Number(str(PI/2-s)[4:],base=10,prec=prec).createNewNumber(prec*2,False)
    elif unit in ['d','D','degre','Degre']:
        return upn.Number(str(90-s*180/PI)[4:],base=10,prec=prec).createNewNumber(prec*2,False)


# atan(x,unit,prec) returns radian or degree value of inverse of tangent of x
# Domain: {R}	Range: -90<=f(x)<=90 or -PI/2<=f(x)<=PI/2
def atan(x=None,unit='d',prec=36):
    if x==None:raise ValueError('Argument of atan() missing')
    if dataType(x) not in ['int','float',str(upn.__name__)+".Number"]:
        raise ValueError("Invalid argument in function atan(x,unit,prec)")
    if unit not in ['d','D','degre','Degre','r','R','c','rad','Rad','radian','Radian']:
        raise Exception('Unit Error.') 
    if dataType(prec)!='int' or prec<1: prec=36

    result=__atan(x,unit,prec)
    return result.createNewNumber(prec,result.isAccurate())


def __atan(x=None,unit='d',prec=36):
    if dataType(x) in ['int','float']:
        x=upn.Number(str(x),base=10,prec=prec,is_accurate=True)
    elif dataType(x)==str(upn.__name__)+".Number":pass
    else: raise ValueError("Invalid argument of atan(x,unit,prec)") 

    PI=pi.getPI(prec)

    if unit in ['d','D','degre','Degre']:
        if x==0:return upn.Number('0',base=10,prec=prec,is_accurate=True)
        elif x==1:return upn.Number('45',base=10,prec=prec,is_accurate=True)
        elif x==-1:return upn.Number('-45',base=10,prec=prec,is_accurate=True)
        elif x>-1 and x<1:
            r=__asin(x/sqrt(1+x*x,prec),'d',prec)
            return upn.Number(str(r)[4:],base=10,prec=prec).createNewNumber(prec*2,False)
        elif x>1:
            r=90-__asin(1/sqrt(1+x*x,prec),'d',prec)
            return upn.Number(str(r)[4:],base=10,prec=prec).createNewNumber(prec*2,False)
        elif x<-1:
            r=__asin(1/sqrt(1+x*x,prec),'d',prec)-90
            return upn.Number(str(r)[4:],base=10,prec=prec).createNewNumber(prec*2,False)
    elif unit in ['r','R','c','rad','Rad','radian','Radian']:
        if x==0:return upn.Number('0',base=10,prec=prec,is_accurate=True)
        elif x==1:return upn.Number(str(PI/4)[4:],base=10,prec=prec).createNewNumber(prec*2,False)
        elif x==-1:return upn.Number(str(-PI/4)[4:],base=10,prec=prec).createNewNumber(prec*2,False)
        elif x>-1 and x<1: 
            r=__asin(x/sqrt(1+x*x,prec2),'r',prec)
            return upn.Number(str(r)[4:],base=10,prec=prec).createNewNumber(prec*2,False)
        elif x>1:
            r=PI/2-__asin(1/sqrt(1+x*x,prec),'r',prec)
            return upn.Number(str(r)[4:],base=10,prec=prec).createNewNumber(prec*2,False)
        elif x<-1:
            r=__asin(1/sqrt(1+x*x,prec),'r',prec)-PI/2
            return upn.Number(str(r)[4:],base=10,prec=prec).createNewNumber(prec*2,False)


# acot(x,unit,prec) returns radian or degree value of inverse of cotangent of x
# Domain: {R}	Range: -90<=f(x)<=90 or -PI/2<=f(x)<=PI/2
def acot(x=None,unit='d',prec=36):
    if x==None:raise ValueError('Argument of acot() missing')
    if dataType(x) not in ['int','float',str(upn.__name__)+".Number"]:
        raise ValueError("Invalid argument in function acot(x,unit,prec)")
    if unit not in ['d','D','degre','Degre','r','R','c','rad','Rad','radian','Radian']:
        raise Exception('Unit Error.') 
    if dataType(prec)!='int' or prec<1: prec=36

    result=__acot(x,unit,prec)
    if dataType(result)==str(upn.__name__)+".Number":
        return result.createNewNumber(prec,result.isAccurate())
    elif dataType(result)=='tuple':
        t=[]
        for num in result:
            t.append(num.createNewNumber(prec,num.isAccurate()))
        return tuple(t)


def __acot(x=None,unit='d',prec=36):
    if dataType(x) in ['int','float']:
        x=upn.Number(str(x),base=10,prec=prec,is_accurate=True)
    elif dataType(x)==str(upn.__name__)+".Number":pass
    else: raise ValueError("Invalid number of acos(x,unit,prec)") 

    PI=pi.getPI(prec)

    if unit in ['d','D','degre','Degre']:
        if x==0:return (upn.Number('90',base=10,prec=prec,is_accurate=True),upn.Number('-90',base=10,prec=prec,is_accurate=True))
        elif x==1:return upn.Number('-45',base=10,prec=prec,is_accurate=True)
        elif x==-1:return upn.Number('45',base=10,prec=prec,is_accurate=True)
        elif x>0 and x<1:
            r=90-__asin(x/sqrt(1+x*x,prec),'d',prec)
            return upn.Number(str(r)[4:],base=10,prec=prec).createNewNumber(prec*2,False)
        elif x<0 and x>-1:
            r=-1*__asin(x/sqrt(1+x*x,prec),'d',prec)-90
            return upn.Number(str(r)[4:],base=10,prec=prec).createNewNumber(prec*2,False)
        elif x>1:
            r=__asin(1/sqrt(1+x*x,prec),'d',prec)
            return upn.Number(str(r)[4:],base=10,prec=prec).createNewNumber(prec*2,False)
        elif x<-1:
            r=-1*__asin(1/sqrt(1+x*x,prec),'d',prec)
            return upn.Number(str(r)[4:],base=10,prec=prec).createNewNumber(prec*2,False)
    elif unit in ['r','R','c','rad','Rad','radian','Radian']:
        if x==0:return ((PI/2).createNewNumber(prec*2,False),(-PI/2).createNewNumber(prec*2,False))
        elif x==1:return (PI/4).createNewNumber(prec*2,False)
        elif x==-1:return (-PI/4).createNewNumber(prec*2,False)
        elif x>0 and x<1:
            r=PI/2-__asin(x/sqrt(1+x*x,prec),'r',prec)
            return upn.Number(str(r)[4:],base=10,prec=prec).createNewNumber(prec*2,False)
        elif x<0 and x>-1:
            r=-1*__asin(x/sqrt(1+x*x,prec),'r',prec)-PI/2
            return upn.Number(str(r)[4:],base=10,prec=prec).createNewNumber(prec*2,False)
        elif x>1:
            r=__asin(1/sqrt(1+x*x,prec),'r',prec)
            return upn.Number(str(r)[4:],base=10,prec=prec).createNewNumber(prec*2,False)
        elif x<-1:
            r=-1*__asin(1/sqrt(1+x*x,prec),'r',prec)
            return upn.Number(str(r)[4:],base=10,prec=prec).createNewNumber(prec*2,False)



# asec(x,unit,prec) returns radian or degree value of inverse of secant of x
# Domain: -1>=x>=1	Range: -180<=f(x)<=180 or -PI<=f(x)<=PI
def asec(x=None,unit='d',prec=36):
    if x==None:raise ValueError('Argument of asec() missing')
    if dataType(x) not in ['int','float',str(upn.__name__)+".Number"]:
        raise ValueError("Invalid argument in function asec(x,unit,prec)")
    if x>-1 and x<1:raise ValueError('Invalid arguments of asec(x). Valid Domain: x>=1 or x<=-1')
    if unit not in ['d','D','degre','Degre','r','R','c','rad','Rad','radian','Radian']:
        raise Exception('Unit Error.') 
    if dataType(prec)!='int' or prec<1: prec=36

    result=__asec(x,unit,prec)
    if dataType(result)==str(upn.__name__)+".Number":
        return result.createNewNumber(prec,result.isAccurate())
    elif dataType(result)=='tuple':
        t=[]
        for num in result:
            t.append(num.createNewNumber(prec,num.isAccurate()))
        return tuple(t)


def __asec(x=None,unit='d',prec=36):
    if dataType(x) in ['int','float']:
        x=upn.Number(str(x),base=10,prec=prec,is_accurate=True)
    elif dataType(x)==str(upn.__name__)+".Number":pass
    else: raise ValueError("Invalid number of acos(x,unit,prec)") 

    PI=pi.getPI(prec)

    if unit in ['d','D','degre','Degre']:
        if x==1:return upn.Number('0',base=10,prec=prec,is_accurate=True)
        elif x==-1:return (upn.Number('180',base=10,prec=prec,is_accurate=True),upn.Number('-180',base=10,prec=prec,is_accurate=True))
        elif x==2:return (upn.Number('60',base=10,prec=prec,is_accurate=True),upn.Number('-60',base=10,prec=prec,is_accurate=True))
        elif x==-2:return (upn.Number('120',base=10,prec=prec,is_accurate=True),upn.Number('-120',base=10,prec=prec,is_accurate=True))
        else:return upn.Number(str(__acos(1/x,'d',prec))[4:],base=10,prec=prec).createNewNumber(prec*2,False)
    elif unit in ['r','R','c','rad','Rad','radian','Radian']:
        if x==1:return upn.Number('0',base=10,prec=prec,is_accurate=True)
        elif x==-1:
            return (upn.Number(str(PI)[4:],base=10,prec=prec,is_accurate=True),upn.Number(str(-PI)[4:],base=10,prec=prec,is_accurate=True))
        elif x==2:
            return (upn.Number(str(PI/3)[4:],base=10,prec=prec).createNewNumber(prec*2,False), \
                upn.Number(str(-PI/3)[4:],base=10,prec=prec).createNewNumber(prec*2,False))
        elif x==-2:
            return (upn.Number(str(2*PI/3)[4:],base=10,prec=prec).createNewNumber(prec*2,False), \
                upn.Number(str(-2*PI/3)[4:],base=10,prec=prec).createNewNumber(prec*2,False))
        else:return upn.Number(str(__acos(1/x,'r',prec))[4:],base=10,prec=prec).createNewNumber(prec*2,False)


# acosec(x,unit,prec) returns radian or degree value of inverse of cosecant of x
# Domain: -1>=x>=1	Range: -180<=f(x)<=180 or -PI<=f(x)<=PI
def acosec(x=None,unit='d',prec=36):
    if x==None:raise ValueError('Argument of acosec() missing')
    if dataType(x) not in ['int','float',str(upn.__name__)+".Number"]:
        raise ValueError("Invalid argument in function acosec(x,unit,prec)")
    if x>-1 and x<1:raise ValueError('Invalid arguments of acosec(x). Valid Domain: x>=1 or x<=-1')
    if unit not in ['d','D','degre','Degre','r','R','c','rad','Rad','radian','Radian']:
        raise Exception('Unit Error.') 
    if dataType(prec)!='int' or prec<1: prec=36

    result=__acosec(x,unit,prec)
    if dataType(result)==str(upn.__name__)+".Number":
        return result.createNewNumber(prec,result.isAccurate())
    elif dataType(result)=='tuple':
        t=[]
        for num in result:
            t.append(num.createNewNumber(prec,num.isAccurate()))
        return tuple(t)

def __acosec(x=None,unit='d',prec=36):
    if dataType(x) in ['int','float']:
        x=upn.Number(str(x),base=10,prec=prec,is_accurate=True)
    elif dataType(x)==str(upn.__name__)+".Number":pass
    else: raise ValueError("Invalid number of acos(x,unit,prec)") 

    PI=pi.getPI(prec)

    if unit in ['d','D','degre','Degre']:
        if x==1:return upn.Number('90',base=10,prec=prec,is_accurate=True)
        elif x==-1:return upn.Number('-90',base=10,prec=prec,is_accurate=True)
        elif x==2:return (upn.Number('30',base=10,prec=prec,is_accurate=True),upn.Number('150',base=10,prec=prec,is_accurate=True))
        elif x==-2:return (upn.Number('-30',base=10,prec=prec,is_accurate=True),upn.Number('-150',base=10,prec=prec,is_accurate=True))
        else:return upn.Number(str(__asin(1/x,'d',prec))[4:],base=10,prec=prec).createNewNumber(prec*2,False)
    elif unit in ['r','R','c','rad','Rad','radian','Radian']:
        if x==1:return upn.Number(str(PI/2)[4:],base=10,prec=prec).createNewNumber(prec*2,False)
        elif x==-1:
            return upn.Number(str(PI/2)[4:],base=10,prec=prec).createNewNumber(prec*2,False)
        elif x==2:
            return (upn.Number(str(PI/6)[4:],base=10,prec=prec).createNewNumber(prec*2,False), \
                upn.Number(str(5*PI/6)[4:],base=10,prec=prec).createNewNumber(prec*2,False))
        elif x==-2:
            return (upn.Number(str(-PI/6)[4:],base=10,prec=prec).createNewNumber(prec*2,False), \
                upn.Number(str(-5*PI/6)[4:],base=10,prec=prec).createNewNumber(prec*2,False))
        else:return upn.Number(str(__asin(1/x,'r',prec))[4:],base=10,prec=prec).createNewNumber(prec*2,False)

# -------------------------- end of triginometric inverse functions -----------------------------




# -------------------------------- Hyperbolic Functions----------------------------
# sinh(x,prec) calculates hyperbolic sine function with high precision
# Domain: {R}		Range: {R}
def sinh(x=None,prec=36):
    if x==None:raise ValueError('Argument of sinh() missing')
    if dataType(prec)!='int' or prec<1: prec=36
    if dataType(x) not in ['int','float',str(upn.__name__)+".Number"]:
        raise ValueError("Invalid argument in function sinh(x,prec)")
    if x==0:return upn.Number('0',10,prec=1,is_accurate=True)
    result=__sinh(x,prec)
    return result.createNewNumber(prec,result.isAccurate())

def __sinh(x=None,prec=36):
    if dataType(x) in ['int','float']:
        return ((__exp(x,prec)-__exp(-1*x,prec))/2).createNewNumber(prec*2,False)
    elif dataType(x)==str(upn.__name__)+".Number":
        return ((_exp(x,prec)-_exp(-1*x,prec))/2).createNewNumber(prec*2,False)


# cosh(x,prec) calculates hyperbolic cosine function with high precision
# Domain: {R}		Range: {R}
def cosh(x=None,prec=36):
    if x==None:raise ValueError('Argument of cosh() missing')
    if dataType(prec)!='int' or prec<1: prec=36
    if dataType(x) not in ['int','float',str(upn.__name__)+".Number"]:
        raise ValueError("Invalid argument in function cosh(x,prec)")
    if x==0:return upn.Number('1',10,prec=1,is_accurate=True)
    result=__cosh(x,prec)
    return result.createNewNumber(prec,result.isAccurate())

def __cosh(x=None,prec=36):
    if dataType(x) in ['int','float']:
        return ((__exp(x,prec)+__exp(-1*x,prec))/2).createNewNumber(prec*2,False)
    elif dataType(x)==str(upn.__name__)+".Number":
        return ((_exp(x,prec)+_exp(-1*x,prec))/2).createNewNumber(prec*2,False)


# tanh(x,prec) calculates hyperbolic tangent function with high precision
# Domain: {R}		Range: {R:-1<=f(x)<=1}
def tanh(x=None,prec=36):
    if x==None:raise ValueError('Argument of tanh() missing')
    if dataType(prec)!='int' or prec<1: prec=36
    if dataType(x) not in ['int','float',str(upn.__name__)+".Number"]:
        raise ValueError("Invalid argument in function tanh(x,prec)")
    if x==0:return upn.Number('0',10,prec=1,is_accurate=True)
    result=__tanh(x,prec)
    return result.createNewNumber(prec,result.isAccurate())

def __tanh(x=None,prec=36):
    if dataType(x) in ['int','float']:
        tmp=__exp(2*x,prec)
        return ((tmp-1)/(tmp+1)).createNewNumber(prec*2,False)
    elif dataType(x)==str(upn.__name__)+".Number":
        tmp=_exp(2*x,prec)
        return ((tmp-1)/(tmp+1)).createNewNumber(prec*2,False)


# coth(x,prec) calculates hyperbolic cotangent function with high precision
# Domain: {R}		Range: {R:-1<=f(x)<=1}
def coth(x=None,prec=36):
    if x==None:raise ValueError('Argument of coth() missing')
    if dataType(prec)!='int' or prec<1: prec=36
    if dataType(x) not in ['int','float',str(upn.__name__)+".Number"]:
        raise ValueError("Invalid argument in function coth(x,prec)")
    if x==0:return upn.Number('0',10,prec=1,is_accurate=True)
    result=__coth(x,prec)
    return result.createNewNumber(prec,result.isAccurate())

def __coth(x=None,prec=36):
    if dataType(x) in ['int','float']:
        tmp=__exp(2*x,prec)
        return ((tmp+1)/(tmp-1)).createNewNumber(prec*2,False)
    elif dataType(x)==str(upn.__name__)+".Number":
        tmp=_exp(2*x,prec)
        return ((tmp+1)/(tmp-1)).createNewNumber(prec*2,False)


# sech(x,prec) calculates hyperbolic secant function with high precision
# Domain: {R}		Range: {R}
def sech(x=None,prec=36):
    if x==None:raise ValueError('Argument of sech() missing')
    if dataType(prec)!='int' or prec<1: prec=36
    if dataType(x) not in ['int','float',str(upn.__name__)+".Number"]:
        raise ValueError("Invalid argument in function sech(x,prec)")
    if x==0:return upn.Number('1',10,prec=1,is_accurate=True)
    result=__sech(x,prec)
    return result.createNewNumber(prec,result.isAccurate())

def __sech(x=None,prec=36):
    if dataType(x) in ['int','float']:
        return (2/(__exp(x,prec)+__exp(-1*x,prec))).createNewNumber(prec*2,False)
    elif dataType(x)==str(upn.__name__)+".Number":
        return (2/(_exp(x,prec)+_exp(-1*x,prec))).createNewNumber(prec*2,False)


# cosech(x,prec) calculates hyperbolic cosecant function with high precision
# Domain: {R}		Range: {R}
def cosech(x=None,prec=36):
    if x==None:raise ValueError('Argument of cosech() missing')
    if dataType(prec)!='int' or prec<1: prec=36
    if dataType(x) not in ['int','float',str(upn.__name__)+".Number"]:
        raise ValueError("Invalid argument in function cosech(x,prec)")
    if x==0:return upn.Number('<inf>',10,prec=1,is_accurate=True)
    result=__cosech(x,prec)
    return result.createNewNumber(prec,result.isAccurate())


def __cosech(x=None,prec=36):
    if dataType(x) in ['int','float']:
        return (2/(__exp(x,prec)-__exp(-1*x,prec))).createNewNumber(prec*2,False)
    elif dataType(x)==str(upn.__name__)+".Number":
        return (2/(_exp(x,prec)-_exp(-1*x,prec))).createNewNumber(prec*2,False)



# ---------------------Hyperbolic Inverse Function----------------------------
# asinh(x,prec) calculates the inverse of the hyperbolic sine function 
# with high precision
# Domain: {R}		Range: {R}
def asinh(x=None,prec=36):
    if x==None:raise ValueError('Argument of asinh() missing')
    if dataType(prec)!='int' or prec<1: prec=36
    if dataType(x) not in ['int','float',str(upn.__name__)+".Number"]:
        raise ValueError("Invalid argument in function asinh(x,prec)")
    result=__asinh(x,prec)
    return result.createNewNumber(prec,result.isAccurate())

def __asinh(x=None,prec=36):
    if dataType(x) in ['int','float']: 
        if x==0:return upn.Number('0',10,prec,True)
        return _ln((x+__sqrt(1+x*x,prec)),prec).createNewNumber(prec*2,False)
    elif dataType(x)==str(upn.__name__)+".Number":
        if x==0:return upn.Number('0',10,prec,True)
        return _ln((x+__sqrt(1+x*x,prec)),prec).createNewNumber(prec*2,False)
    else:raise ValueError("Invalid arguement of __asinh(x.prec)")


# acosh(x,prec) calculates the inverse of the hyperbolic cosine function 
# with high precision
# Domain: {R:-1>=x>=1}		Range: {R}
def acosh(x=None,prec=36):
    if x==None:raise ValueError('Argument of acosh() missing')
    if dataType(prec)!='int' or prec<1: prec=36
    if dataType(x) not in ['int','float',str(upn.__name__)+".Number"]:
        raise ValueError("Invalid argument in function acosh(x,prec)")
    result=__acosh(x,prec)
    return result.createNewNumber(prec,result.isAccurate())

def __acosh(x=None,prec=36):
    if x<1:return upn.Number('<undefined>',10,0,True)
    if dataType(x) in ['int','float']:  
        if x==1:return upn.Number('0',10,prec,True)      
        return _ln((x+__sqrt(x*x-1,prec)),prec).createNewNumber(prec*2,False)
    elif dataType(x)==str(upn.__name__)+".Number":
        return _ln((x+__sqrt(x*x-1,prec)),prec).createNewNumber(prec*2,False)
    else:raise ValueError("Invalid arguement of __acosh(x.prec)")


# atanh(x,prec) calculates the inverse of the hyperbolic tangent function 
# with high precision
# Domain: {R:-1>=x>=1}		Range: {R}
def atanh(x=None,prec=36):
    if x==None:raise ValueError('Argument of acosh() missing')
    if dataType(prec)!='int' or prec<1: prec=36
    if dataType(x) not in ['int','float',str(upn.__name__)+".Number"]:
        raise ValueError("Invalid argument in function atanh(x,prec)")
    result=__atanh(x,prec)
    return result.createNewNumber(prec,result.isAccurate())

def __atanh(x=None,prec=36):
    if x>1 or x<-1:return upn.Number('<undefined>',10,0,True)
    if dataType(x) in ['int','float']:  
        if x==1:return upn.Number('<inf>',10,prec,True)
        elif x==-1:return upn.Number('<-inf>',10,prec,True)
        return 0.5*_ln(upn.Number(str(1+x),10,prec)/upn.Number(str(1-x),10,prec),\
        prec).createNewNumber(prec*2,False)
    elif dataType(x)==str(upn.__name__)+".Number":
        if x==1:return upn.Number('<inf>',10,prec,True)
        elif x==-1:return upn.Number('<-inf>',10,prec,True)
        return 0.5*_ln((1+x)/(1-x),prec).createNewNumber(prec*2,False)
    else:raise ValueError("Invalid arguement of __atanh(x.prec)")


# acoth(x,prec) calculates the inverse of the hyperbolic cotangent function 
# with high precision
# Domain: {R:-1>=x>=1}		Range: {R}
def acoth(x=None,prec=36):
    if x==None:raise ValueError('Argument of acosh() missing')
    if dataType(prec)!='int' or prec<1: prec=36
    if dataType(x) not in ['int','float',str(upn.__name__)+".Number"]:
        raise ValueError("Invalid argument in function acoth(x,prec)")
    result=__acoth(x,prec)
    return result.createNewNumber(prec,result.isAccurate())

def __acoth(x=None,prec=36):
    if x<1 and x>-1:return upn.Number('<undefined>',10,0,True)
    if dataType(x) in ['int','float']:  
        if x==1:return upn.Number('<inf>',10,prec,True)
        if x==-1:return upn.Number('<-inf>',10,prec,True)
        return 0.5*_ln(upn.Number(str(x+1),10,prec)/upn.Number(str(x-1),10,prec),\
        prec).createNewNumber(prec*2,False)
    elif dataType(x)==str(upn.__name__)+".Number":
        if x==1:return upn.Number('<inf>',10,prec,True)
        if x==-1:return upn.Number('<-inf>',10,prec,True)
        return 0.5*_ln((x+1)/(x-1),prec).createNewNumber(prec*2,False)
    else:raise ValueError("Invalid arguement of __acoth(x.prec)")


# asech(x,prec) calculates the inverse of the hyperbolic secant function 
# with high precision
# Domain: {R:1>=x>=0}		Range: {R}
def asech(x=None,prec=36):
    if x==None:raise ValueError('Argument of acosh() missing')
    if dataType(prec)!='int' or prec<1: prec=36
    if dataType(x) not in ['int','float',str(upn.__name__)+".Number"]:
        raise ValueError("Invalid argument in function asech(x,prec)")
    result=__asech(x,prec)
    return result.createNewNumber(prec,result.isAccurate())

def __asech(x=None,prec=36):
    if x<0 or x>1:return upn.Number('<undefined>',10,0,True)
    if dataType(x) in ['int','float']:  
        if x==1:return upn.Number('0',10,prec,True)
        if x==0:return upn.Number('<inf>',10,prec,True)
        return _ln((1+__sqrt(1-x*x))/x,prec).createNewNumber(prec*2,False)
    elif dataType(x)==str(upn.__name__)+".Number":
        if x==1:return upn.Number('0',10,prec,True)
        if x==0:return upn.Number('<inf>',10,prec,True)
        return _ln((1+__sqrt(1-x*x))/x,prec).createNewNumber(prec*2,False)
    else:raise ValueError("Invalid arguement of __asech(x.prec)")

# acosech(x,prec) calculates the inverse of the hyperbolic cosecant function 
# with high precision
# Domain: {R:1>=x>=0}		Range: {R}
def acosech(x=None,prec=36):
    if x==None:raise ValueError('Argument of acosh() missing')
    if dataType(prec)!='int' or prec<1: prec=36
    if dataType(x) not in ['int','float',str(upn.__name__)+".Number"]:
        raise ValueError("Invalid argument in function acosech(x,prec)")
    result=__acosech(x,prec)
    return result.createNewNumber(prec,result.isAccurate())

def __acosech(x=None,prec=36):
    if x<0:return upn.Number('<undefined>',10,0,True)
    if dataType(x) in ['int','float']:  
        if x==0:return upn.Number('<inf>',10,prec,True)
        return _ln((1+__sqrt(1+x*x))/x,prec).createNewNumber(prec*2,False)
    elif dataType(x)==str(upn.__name__)+".Number":
        if x==0:return upn.Number('<inf>',10,prec,True)
        return _ln((1+__sqrt(1+x*x))/x,prec).createNewNumber(prec*2,False)
    else:raise ValueError("Invalid arguement of __acosech(x.prec)")

# --------------------------End of Hyperbolic Functions---------------------------

# ----------------------------Other Standard Functions----------------------------
# gamma(x) function returns approximate value of gamma of x
# T(z)=Int((t^(z-1))*e^(-t)dt),0,inf)
# Method name: Lanczos Apprximation Algorithm (Numerical recepies in C, 
# Cambridge University Press,1992) 
# Domain: {R:x>0}		Range: {R:f(x)>=0}
def gamma(x=None,prec=36):
    if x==None:raise ValueError('Argument of gamma2() missing')
    if dataType(prec)!='int' or prec<1: prec=36
    if dataType(x) not in ['int','float',str(upn.__name__)+".Number"]:
        raise ValueError("Invalid argument in function gamma(x,prec)")
    if dataType(prec)!='int' or prec<1: prec=36
    result=__gamma(x,prec)
    return result.createNewNumber(prec,result.isAccurate())

def __gamma(x=None,prec=36):
    if x<0:raise ValueError('Unable to calculate gamma(x,prec) in this domain,x<0.')
    if x==0:return upn.Number('<inf>',10,1,True)
    elif x==1 or x==2:return upn.Number('1',10,1,True)

    if dataType(x)=='int':
        return upn.Number(str(__fact(x-1)),10,prec,True)
    elif dataType(x)=='float':
        x=upn.Number(str(x),10,prec,False)
    elif dataType(x)==str(upn.__name__)+".Number":
        if x.isInteger() and x.getBase()==10:
            return upn.Number(str(__fact(int(x.getNormalizedPart()['ipart'])-1)),10,prec,True)
        elif x.isInteger() and x.getBase() in [2,8,16,32,64]:
            return upn.Number(str(__fact(int(x.getBase10Part()['ipart'])-1)),10,prec,True)
    else:raise ValueError("Invalid arguement of __gamma(x.prec)")

    if prec<=36: prec2=prec+4
    elif prec>36:prec2=int(1.1*prec)

    c0=1.000000000190015
    coeff=[76.18009172947146,-86.50532032941677,24.01409824083091,\
-1.231739572450155,0.001208650973866179,-0.000005395239384953]
    s=0
    for i in range(1,7):s+=coeff[i-1]/(x+i) 
    s=c0+s;
    tmp=__sqrt(2*pi.getPI(prec2),prec2)*s*__power(x+5.5,x+0.5,prec2)*_exp(-5.5-x,prec2)/x
    return tmp.createNewNumber(prec2*2,False)


# erf(x,prec) returns the integral Int(e^(-t^2)dt) in the interval 
# from 0 to x with high precision
# Domain:{R}	Range:{R:-1<=f(x)<=1}
def erf(x=None,prec=36):
    if x==None:raise ValueError('Argument of erf() missing')
    if dataType(x) not in ['int','float',str(upn.__name__)+".Number"]:
        raise ValueError("Invalid argument in function erf(x,prec)")
    if dataType(prec)!='int' or prec<1: prec=36
    result=__erf(x,prec)
    return result.createNewNumber(prec,result.isAccurate())

def __erf(x=None,prec=36):
    if dataType(x) in ['int','float']:
        x=upn.Number(str(x),10,prec,False)
    elif dataType(x)==str(upn.__name__)+".Number":pass
    else:raise ValueError("Invalid arguement of __gamma(x.prec)")

    if x==0:return upn.Number('0',base=10,prec=prec,is_accurate=True)
    elif x>10:return upn.Number('1',base=10,prec=prec,is_accurate=True)
    elif x<-10:return upn.Number('-1',base=10,prec=prec,is_accurate=True)

    delP=upn.Number('1p-'+str(prec),10,prec=prec)
    if prec<40: prec2=prec+4
    else:prec2=int(1.1*prec)

    i=1
    t,s=x.copy(),x.copy()	# initialization of term and sum
    while(True):        
        t=t*(-1)*x*x*(2*i-1)/(2*i*i+i)
        if t.getPrecision()>3*prec2:
            t=t.createNewNumber(prec2*2,False)
        if t>0 and t<delP: break
        elif t<0 and -1*t<delP: break
        s=s+t
        i=i+1
    m=2/__sqrt(pi.getPI(prec2))
    return (s*m).createNewNumber(prec2*2,False)


# erfc(x,prec) returns the complementary error function of x (1-erf(X))
# in the interval from 0 to x with high precision
# Domain:{R}	Range:{R:0<=f(x)<=2}
def erfc(x=None,prec=36):
    if x==None:raise ValueError('Argument of erf() missing')
    if dataType(x) not in ['int','float',str(upn.__name__)+".Number"]:
        raise ValueError("Invalid argument in function erfc(x,prec)")
    if dataType(prec)!='int' or prec<1: prec=36
    result=1-__erf(x,prec)
    return result.createNewNumber(prec,result.isAccurate())



# beta(x,y) is called beta function defined by Int(t^(x-1)*(1-t)^(y-1)dt)
# in the interval [0,1] which is equal to gamma(x)*gamma(y)/gamma(x+y)
# Domain:{R:x>=0,y>=0}	Range:{R:0<=f(x)<=1}
def beta(x=None,y=None,prec=36):
    if x==None or y==None:raise ValueError('Argument of beta() missing')
    if dataType(x) not in ['int','float',str(upn.__name__)+".Number"]:
        raise ValueError("Invalid argument in function beta(x,y,prec)")
    if dataType(prec)!='int' or prec<1: prec=36
    result=__beta(x,y,prec)
    return result.createNewNumber(prec,result.isAccurate())

def __beta(x=None,y=None,prec=36):
    if dataType(x) in ['int','float']:
        x=upn.Number(str(x),10,prec,False)
    elif dataType(x)==str(upn.__name__)+".Number":pass
    else:raise ValueError("Invalid arguement of __gamma(x.prec)")
    if x<0 or y<0:raise ValueError('Invalid argument of beta(x,y) [x>0,y>0].')
    if x==0 or y==0:return upn.Number('<inf>',base=10,prec=prec,is_accurate=True)

    return __gamma(x)*__gamma(y)/__gamma(x+y)




# ------------------------ Numbers of Number Theory ----------------------------
# eulerNumber(r) calculates and returns the euler number of the given positive 
# integer by double sum method
# SUM(((-1)^i*(SUM(((-1)^j*nCr(2i,j)*(i-j)^r),j=0,j=2i))/2^i),i=1,i=r)
# r=0,1,2,3,4,5,6,7,8,9,10
# E(r)=1,0,-1,0,5,0,-61,0,1385,0,-50521
# >>> smf.eulerNumber(18)
# b10:-2404879675441
def eulerNumber(r=None):
    if r==None:raise ValueError('Argument of eulerNumber() missing')
    if dataType(r) not in ['int','float',str(upn.__name__)+".Number"]:
        raise ValueError("Invalid argument in function eulerNumber(r)")
    if dataType(r)=='int' and r>=0:k=r
    elif dataType(r)==str(upn.__name__)+'.Number' and r.isInteger():
        k=r.toDenaryInteger() 
    else: raise ValueError('Argument of eulerNumber() is not a positive integer')

    if k==0:return upn.Number('1',10,prec=1,is_accurate=True)
    elif k%2==1:return upn.Number('0',10,prec=1,is_accurate=True) #returns 0 if k is odd
  
    p1=1;p=1;sum1=0;sum2=0;i=1   
    while True:
        if i%2==0:neg1=1
        else:neg1=-1

        sum2=0;p2=1
        for j in range(0,2*i+1):
            if j%2==0:neg2=1
            else:neg2=-1
            p2=neg2*(nCr(2*i,j).toDenaryInteger())*((i-j)**k)
            sum2=sum2+p2
        p=neg1*sum2/2**i
        sum1=sum1+p
        if i>=k:break
        i=i+1
    return upn.Number(str(sum1),10,is_accurate=True) 

# bernoulliNumber(r) calculates and returns the Bernoulli number of the given positive 
# integer (2,4,6,...) by the following definition
# B(r)=0 if r is an odd positive integer
# SUM((nCr(r-1,i)*r*E(r)/(4^r-2^r)),i=0,i=r-1)
# r=1,2,3,4,5,6,7,8,9,10
# B(r)=0,1/6,0,-1/30,0,1/42,0,-1/30,0,5/66
# >>> smf.eulerNumber(18)
# b10:-2404879675441
def bernoulliNumber(r=None):
    if r==None:raise ValueError('Argument of eulerNumber() missing')
    if dataType(r) not in ['int','float',str(upn.__name__)+".Number"]:
        raise ValueError("Invalid argument in function bernoulliNumber(r)")
    if dataType(r)=='int' and r>0:k=r
    elif dataType(r)==str(upn.__name__)+'.Number' and r.isInteger():
        k=r.toDenaryInteger() 
    else: raise ValueError('Argument of bernoulliNumber() is not a positive integer and greater than 0')

    if k%2==1:return upn.Number('0',10,prec=1,is_accurate=True) #returns 0 if k is odd

    SUM=0 #upn.Number('0',10,is_accurate=True)
    deno=4**k-2**k
    for i in range(0,k,2):        
        SUM=SUM+nCr(k-1,i).toDenaryInteger()*k*eulerNumber(i).toDenaryInteger()
    return upn.Number(str(SUM)+'/'+str(deno),10,modify=True)

# tangentNumber(r) calculates and returns the Tangent number of the given positive 
# and even integer (2,4,6,...) by the following definition
# T(r)=0 if r is an odd positive integer
# 2^r*2^(r-1)*B(r)
# r=0,1,2,3,4,5,6,7,8,9,10
# T(r)=1,0,-1,0,5,0,-61,0,1385,0,-50521
# >>> smf.bernoulliNumber(18)
# b10:54 775/798
def tangentNumber(r=None):
    if r==None:raise ValueError('Argument of eulerNumber() missing')
    if dataType(r) not in ['int','float',str(upn.__name__)+".Number"]:
        raise ValueError("Invalid argument in function tangentNumber(r)")
    if dataType(r)=='int' and r>0:k=r
    elif dataType(r)==str(upn.__name__)+'.Number' and r.isInteger():
        k=r.toDenaryInteger() 
    else: raise ValueError('Argument of bernoulliNumber() is not a positive integer and greater than 0')
    if k%2==1:return upn.Number('0',10,prec=1,is_accurate=True) #returns 0 if k is odd

    SUM=0 #upn.Number('0',10,is_accurate=True)
    p=2**k;deno=(4**k-p)*k
    for i in range(0,k,2):        
        SUM=SUM+nCr(k-1,i).toDenaryInteger()*k*eulerNumber(i).toDenaryInteger()
    SUM=upn.Number(str(SUM),10,is_accurate=True)
    tval=0
    if (k//2)%2==0:tval=(-1*p*(p-1))*SUM/deno
    elif (k//2)%2==1:tval=(p*(p-1))*SUM/deno
    return tval





