"""
Author: Engr. A.K.M. Aminul Islam
Date: 2020,Jun,25
Version:2.0.2020.06.25
Description: The function __getE() creates the value of e or E
correct to the given precision level
getE(100)=b10:2.7182818284590452353602874713526624977572470
936999595749669676277240766303535475945713821785251664274
"""
from __future__ import division
from . import upNumber as upn

__version__='2.0.2020.06.25'

# getE(prec) returns the exponential value of e='exp(1)'
# e=1+1/1!+1/2!+1/3!+...
# >>> pe.getE()
# b10:2.7182818284590452353602874713526625
def getE(prec=36):
    if dataType(prec)!='int' and prec<6: prec=36
    delP=upn.Number('1p-'+str(prec),10,prec=prec);
    if prec<25: prec2=prec+4
    else:prec2=int(1.1*prec)
    SUM=upn.Number('2',10,prec=prec2);
    t1=upn.Number('1',10,prec=prec2);
    c=upn.Number('1',10,prec=prec2);	# t=term, c=counter   
    i=0 
    while(True):
        t2=t1/(c+1);SUM=SUM+t2
        if t1-t2<delP:break
        t1=t2;c=c+1;
        i=i+1
    return upn.Number(str(SUM)[4:],10).createNewNumber(prec=prec,is_accurate=False)

# dataType() function returns the type of a data
# type(2.0) returns "(type 'float')"
def dataType(data=None):
    s=str(type(data)).split(' ')[1]
    return s.split("'")[1]



