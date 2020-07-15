"""
   Author:Engr. A.K.M. Aminul Islam   
   Description:This module returns the value of PI either through
               a public variable or getPI(prec=36) function
      t=sum(0.015625*(256/(10*i+1)+1/(10*i+9)-32/(4*i+1)-1/(4*i+3)-64/(10*i+3)-4/(10*i+5)-4/(10*i+7))/d)
      where i=0,1,2,3,...
   Location:\pmath\pi.py
   Date of Last Edit:25th Jun,2020 (Version 2.1.2020.07.13)
   Module Code:CPY-2-1-2020-07-13
   >>> pi.getPI(100)
   b10:3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
"""
from __future__ import division
from . import upNumber as upn

__version__='2.1.2020.07.13'


# Calculating pi using Bellard's Formula (most efficient formula)
# It takes 14 iterations to produce a number correct to 34 d.p.
# It is the precision version of getPI() function
def getPI(prec=36):
    if dataType(prec)!='int': prec=36
    delP=upn.Number('1p-'+str(prec),10,prec=prec)

    if prec<100: prec2=prec+4
    else:prec2=int(1.05*prec)

    SUM=upn.Number('0',10,prec=prec2);
    t=upn.Number('1.0',10,prec=prec2)
    sign=1;i=0;deno=64

    while(t > delP):        
        a=upn.Number(str(10*i+1),10,prec=prec2)
        b=upn.Number(str(10*i+9),10,prec=prec2)
        c=upn.Number(str(4*i+1),10,prec=prec2)
        d=upn.Number(str(4*i+3),10,prec=prec2)
        e=upn.Number(str(10*i+3),10,prec=prec2)
        f=upn.Number(str(10*i+5),10,prec=prec2)
        g=upn.Number(str(10*i+7),10,prec=prec2)

        t=((256/a)+(1/b)-(32/c)-(1/d)-(64/e)-(4/f)-(4/g))/deno
        deno=deno*1024
        SUM=SUM+t*sign
        if sign==1:sign=-1
        elif sign==-1:sign=1
        i+=1; 

    return upn.Number(str(SUM)[4:],10,prec=prec2).createNewNumber(prec=prec,is_accurate=False) 


# dataType() function returns the type of a data
# type(2.0) returns "(type 'float')"
def dataType(data=None):
    s=str(type(data)).split(' ')[1]
    return s.split("'")[1]


## ******************************************************************
















