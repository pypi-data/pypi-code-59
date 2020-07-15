"""
    Module Name: Number (universal precision number)
    Author: Engr. A.K.M. Aminul Islam
    Date: 2020,July,15
    Version:1.0.2020.07.15
    Description:This module contains the functions needed for handling numbers of
        any type and many bases. The functions of this module can convert a number 
        of a base 2,8,10,16,32,64 to base 2,8,10,16,32,64. It can create a number
        with the accuracy to the desired precision level. All numbers are returned 
        and manipulated in string format. It can handle integer and floating 
        point numbers of any base from 2,8,10,16,32,64. This module can process
        any number from ultra small to ultra large level.

        The central number system is binary and denary. Numbers of bases 8,16,32 and 64 are
        converted efficiently through binary. Number arithmetic operations are performed by 
        denary (base10) arithmetic operations.

        Number data are stored in a dictionary data format.
        (base='bXX', sign='','+','-' ipart=integer part, fpart=floating part,
         expo=exponent, numerator, deno=denominator)

    Information on the module content		Numeric Output		Digits
    Base=2	Binary Number			b02:-11001.011p600	0,1
    Base=8	Octal Number			b08:-4572.0273p-600	0-7
    Base=10	Denary Number			b10:-9078.0412p40	0-9
    Base=16	Hexadecimal Number		b16:-f04d.32abp70	0-9a-fA-F
    Base=32	DuoTrigesimal/base32 Number	b32:-vV0o.25f9p+147	0-9a-vA-V
    Base=64	base64 Number			b64:-zXo0.a4Btp-250	0-9a-zA-Z!@

    Number showing modes (show_mode):'fp' and 'fr'
	'fp' (floating point) mode means numbers with floating digits.
		Like:b02:-11110001.11p-10,b10:92.45e33
	'fr' (fractional) mode which displays number as mixed or proper fraction.
		Like:b02:-11110001 11/100p+17, b10:92 9/20e+23.
	Difference: 'fp' numbers contain '.', but 'fr' numbers have '/'.

    ***If a floating or fractional number is recurring, this module can handle it
    very efficiently. Recurring floatings can be converted into recurring fractions.

    Valid Input Format: (fp)11110.101,11110.101p+34,11110.101p34,11110.101p-23, -0.1101p-45
		(fr) '-1101 11/1101', "-1101 11/1101p+7", "-1101 11/1101p7", '-1101 11/1101p-17'

    Location:cpysoft/upmath/Number.py
    Function naming type: camel case like isBinary()
    Class naming style=Starting with upper case + camel case
    Date of Last Edit:15th July,2020 (Version 1.1.2020.07.15)
    Module Code:NUMBER-1-1-2020-07-15
"""
from __future__ import division
from . import upNumber
from . import psmf

__version__='1.1.2020.07.15'


# dataType() function returns the type of a data
# type(2.0) returns "(type 'float')"
def dataType(data=None):
    s=str(type(data)).split(' ')[1]
    return s.split("'")[1]


# class Number is derived from upn.Number to have power and other
# standard math functions
class Number(upNumber.Number):
    __parent=None


    def __init__(self,num=None,base=10,prec=36,is_accurate=True,modify=False,ultraModify=False):
        super().__init__(num,base,prec,is_accurate,modify,ultraModify)
        self.__parent=super().copy()
        #print(self,self.__parent)



    def getParent(self): return self.__parent




    # ------------------------------------------------------------------
    # arithmetic operations (+,-,*,/,//,%,**)
    # ------------------------------------------------------------------
    # To add two numbers (a+b,a+7,a+2.56)
    def __add__(self,right):
        if dataType(right) in ['int','float',str(upNumber.__name__)+'.Number']:
            tmp=self.__parent.__add__(right)
            return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())
        elif dataType(right)==str(__name__)+'.Number':
            tmp=self.__parent.__add__(right.__parent)
            return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())
        else: raise TypeError("Invalid operand of the operator '+'")
    # addition:10+a or 10.25+a (left+self)
    def __radd__(self,left):
        if dataType(left) in ['int','float',str(upNumber.__name__)+'.Number']:
            tmp=self.__parent.__add__(left)
            return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())
        elif dataType(left)==str(__name__)+'.Number':
            tmp=self.__parent.__add__(left.__parent)
            return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())
        else: raise TypeError("Invalid operand of the operator '+'")

    # To subtract two numbers (a-b,a-7,a-2.56)
    def __sub__(self,right):
        if dataType(right) in ['int','float',str(upNumber.__name__)+'.Number']:
            tmp=self.__parent.__sub__(right)
            return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())
        elif dataType(right)==str(__name__)+'.Number':
            tmp=self.__parent.__sub__(right.__parent)
            return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())
        else: raise TypeError("Invalid operand of the operator '-'")
    # left subtraction: 10-a or 10.25-a (left - self)
    def __rsub__(self,left):
        if dataType(left) in ['int','float',str(upNumber.__name__)+'.Number']:
            a=self.__sub__(left)
            if a.__parseddict['sign']=='+':a.__parseddict['sign']='-'
            elif a.__parseddict['sign']=='-':a.__parseddict['sign']='+'
            return Number(str(a)[4:],10,self.getMaxPrecision(),self.isAccurate())
        elif dataType(left)==str(__name__)+'.Number':
            a=self.__parent.__sub__(left.__parent)
            if a.__parseddict['sign']=='+':a.__parseddict['sign']='-'
            elif a.__parseddict['sign']=='-':a.__parseddict['sign']='+'
            return Number(str(a)[4:],10,self.getMaxPrecision(),self.isAccurate())
        else: raise TypeError("Invalid operand of the operator '-'")

    # __abs__()
    def __abs__(self):
        tmp=self.__parent.__abs__()
        return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())

    # multiplying two numbers: a*b, a*10, a*10.5, a*12e+7
    def __mul__(self,right):
        if dataType(right) in ['int','float',str(upNumber.__name__)+'.Number']:
            tmp=self.__parent.__mul__(right)
            return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())
        elif dataType(right)==str(__name__)+'.Number':
            tmp=self.__parent.__mul__(right.__parent)
            return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())
        else: raise TypeError("Invalid operand of the operator '*'")
    # left multiplication:10*a or 10.25*a (left * self)
    def __rmul__(self,left):
        if dataType(left) in ['int','float',str(upNumber.__name__)+'.Number']:
            tmp=self.__parent.__mul__(left)
            return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())
        elif dataType(left)==str(__name__)+'.Number':
            tmp=self.__parent.__sub__(left.__parent)
            return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())
        else: raise TypeError("Invalid operand of the operator '*'")

    # dividing two numbers: a/b, a/10, a/10.5, a/12e+7
    def __truediv__(self,right):
        if dataType(right) in ['int','float',str(upNumber.__name__)+'.Number']:
            tmp=self.__parent.__truediv__(right)
            return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())
        elif dataType(right)==str(__name__)+'.Number':
            tmp=self.__parent.__truediv__(right.__parent)
            return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())
        else: raise TypeError("Invalid operand of the operator '/'")
    # left division:10/a or 10.25/a (left / self)
    def __rtruediv__(self,left):
        if dataType(left) in ['int','float']:
            #tmp=left/self.__parent
            tmp=self.__parent.__rtruediv__(left)
            return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())
        elif dataType(left)==str(upNumber.__name__)+'.Number':
            tmp=left.__truediv__(self.__parent)
            return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())
        else: raise TypeError("Invalid operand of the operator '/'")
    # dividing two numbers: a//b, a//10, a//10.5, a//12e+7
    def __floordiv__(self,right):
        if dataType(right) in ['int','float',str(upNumber.__name__)+'.Number']:
            tmp=self.__parent.__floordiv__(right)
            return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())
        elif dataType(right)==str(__name__)+'.Number':
            tmp=self.__parent.__floordiv__(right.__parent)
            return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())
        else: raise TypeError("Invalid operand of the operator '//'")
    # left division:10//a or 10.25//a (left // self)
    def __rfloordiv__(self,left):
        if dataType(left) in ['int','float']:
            #tmp=left//self.__parent
            tmp=self.__parent.__rfloordiv__(left)
            return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())
        elif dataType(left)==str(upNumber.__name__)+'.Number':
            tmp=psmf.power(self.__parent,right.__parent,prec)
            return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())
            return left.__floordiv__(self.__parent)
        else: raise TypeError("Invalid operand of the operator '//'")

    # remainder operation between two numbers: a%b, a%10, a%10.5, a%12e+7
    def __mod__(self,right):
        if dataType(right) in ['int','float',str(upNumber.__name__)+'.Number']:
            tmp=self.__parent.__mod__(right)
            return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())
        elif dataType(right)==str(__name__)+'.Number':
            tmp=self.__parent.__mod__(right.__parent)
            return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())
        else: raise TypeError("Invalid operand of the operator '%'")
    def __rmod__(self,left):
        if dataType(left) in ['int','float',str(upNumber.__name__)+'.Number']:
            tmp=self.__parent.__rmod__(left)
            return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())
        elif dataType(left)==str(__name__)+'.Number':
            tmp=self.__parent.__rmod__(left.__parent)
            return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())
        else: raise TypeError("Invalid operand of the operator '%'")

    # inverse operation: inv(a)
    def __inv__(self):
        if self.__parseddict['ipart']=='<INF>': return Number('0',10,1,True)
        elif self.__parseddict['ipart']=='<UNDEFINED>': return Number('<undefined>',10,0,True)
        elif self.__parseddict['ipart']=='0' and self.__parseddict['fpart']=='0' and self.__parseddict['sign']=='+':
            return Number('<inf>',10,1,True)
        elif self.__parseddict['ipart']=='0' and self.__parseddict['fpart']=='0' and self.__parseddict['sign']=='-':
            return Number('<-inf>',10,1,True)
        tmp=self.__parent.__inv__()
        return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())

    # power operation: a**b, a**3, a**-2.5, a**-3
    def __pow__(self,right,prec=36):
        if dataType(right) in ['int','float',str(upNumber.__name__)+'.Number']:
            tmp=psmf.power(self.__parent,right,prec)
            return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())
        elif dataType(right)==str(__name__)+'.Number':
            tmp=psmf.power(self.__parent,right.__parent,prec)
            return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())
        else: raise TypeError("Invalid operand of the operator '**'")
    # power operation: a**b, a**3, a**-2.5, a**-3
    def __rpow__(self,left,prec=36):
        if dataType(left) in ['int','float',str(upNumber.__name__)+'.Number']:
            tmp=psmf.power(left,self.__parent,prec)
            return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())
        elif dataType(left)==str(__name__)+'.Number':
            tmp=psmf.power(left.__parent,self.__parent,prec)
            return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())
        else: raise TypeError("Invalid operand of the operator '**'")


    # end of arithmetic operators #
    # ------------------------------------------------------------------

    # ------------------------------------------------------------------
    # logical operations (==,!=,>,>=,<,<=)
    # ------------------------------------------------------------------
    # comparison operator: equal_to (==); a==b, b==a, a==10, b==10.67
    def __eq__(self,right):
        if dataType(right) in ['int','float',str(upNumber.__name__)+'.Number']:
            return self.__parent.__eq__(right)
        elif dataType(right)==str(__name__)+'.Number':
            return self.__parent.__eq__(right.__parent)
        else: raise TypeError("Invalid operand of the operator '=='")
    # comparison operator: left equal_to (==); 10==a, 10.67==b
    def __req__(self,left):
        if dataType(left) in ['int','float',str(upNumber.__name__)+'.Number']:
            return self.__parent.__req__(left)
        elif dataType(left)==str(__name__)+'.Number':
            return self.__parent.__req__(left.__parent)
        else: raise TypeError("Invalid operand of the operator '=='")

    # comparison operator: not equal_to (!=); a!=b, a!=10, a!=10.67
    def __ne__(self,right):
        if dataType(right) in ['int','float',str(upNumber.__name__)+'.Number']:
            return self.__parent.__ne__(right)
        elif dataType(right)==str(__name__)+'.Number':
            return self.__parent.__ne__(right.__parent)
        else: raise TypeError("Invalid operand of the operator '!='")
    # comparison operator: left not equal_to (!=); 10!=a, 10.67!=a
    def __rne__(self,left):
        if dataType(left) in ['int','float',str(upNumber.__name__)+'.Number']:
            return self.__parent.__rne__(left)
        elif dataType(left)==str(__name__)+'.Number':
            return self.__parent.__rne__(left.__parent)
        else: raise TypeError("Invalid operand of the operator '!='")

    # comparison operator: greater_than (>); a>b, b>a, a>10, b>10.67
    def __gt__(self,right):
        if dataType(right) in ['int','float',str(upNumber.__name__)+'.Number']:
            return self.__parent.__gt__(right)
        elif dataType(right)==str(__name__)+'.Number':
            return self.__parent.__gt__(right.__parent)
        else: raise TypeError("Invalid operand of the operator '>'")
    # comparison operator: left greater_than (>); 10>a, 10.67>b
    def __rgt__(self,left):
        if dataType(left) in ['int','float',str(upNumber.__name__)+'.Number']:
            return self.__parent.__rgt__(left)
        elif dataType(left)==str(__name__)+'.Number':
            return self.__parent.__rgt__(left.__parent)
        else: raise TypeError("Invalid operand of the operator '>'")

    # comparison operator: greater_than (>); a>b, b>a, a>10, b>10.67
    def __lt__(self,right):
        if dataType(right) in ['int','float',str(upNumber.__name__)+'.Number']:
            return self.__parent.__lt__(right)
        elif dataType(right)==str(__name__)+'.Number':
            return self.__parent.__lt__(right.__parent)
        else: raise TypeError("Invalid operand of the operator '<'")
    # comparison operator: left greater_than (>); 10>a, 10.67>b
    def __rlt__(self,left):
        if dataType(left) in ['int','float',str(upNumber.__name__)+'.Number']:
            return self.__parent.__rlt__(left)
        elif dataType(left)==str(__name__)+'.Number':
            return self.__parent.__rlt__(left.__parent)
        else: raise TypeError("Invalid operand of the operator '<'")

    # comparison operator: less_than or equal_to (<); a<=b, a<=10, a<=10.67
    def __le__(self,right):
        if dataType(right) in ['int','float',str(upNumber.__name__)+'.Number']:
            return self.__parent.__le__(right)
        elif dataType(right)==str(__name__)+'.Number':
            return self.__parent.__le__(right.__parent)
        else: raise TypeError("Invalid operand of the operator '<='")
    # comparison operator: less_than or equal_to (<); a<=b, 10<=a, 10.67<=a
    def __rle__(self,left):
        if dataType(left) in ['int','float',str(upNumber.__name__)+'.Number']:
            return self.__parent.__rle__(left)
        elif dataType(left)==str(__name__)+'.Number':
            return self.__parent.__rle__(left.__parent)
        else: raise TypeError("Invalid operand of the operator '<='")

    # comparison operator: greater_than or equal_to (>=); a>=b, a>=10, a>=10.67
    def __ge__(self,right):
        if dataType(right) in ['int','float',str(upNumber.__name__)+'.Number']:
            return self.__parent.__ge__(right)
        elif dataType(right)==str(__name__)+'.Number':
            return self.__parent.__ge__(right.__parent)
        else: raise TypeError("Invalid operand of the operator '>='")
    # comparison operator: less_than or equal_to (>=); a>=b, 10>=a, 10.67>=a
    def __rge__(self,left):
        if dataType(left) in ['int','float',str(upNumber.__name__)+'.Number']:
            return self.__parent.__rge__(left)
        elif dataType(left)==str(__name__)+'.Number':
            return self.__parent.__rge__(left.__parent)
        else: raise TypeError("Invalid operand of the operator '>='")

    # end of logical operators #
    # ------------------------------------------------------------------

    # ------------------------------------------------------------------
    # in-place operators (+=, -=, *=, /=, //=, %=)
    # ------------------------------------------------------------------
    # in-place addition operator (+=): a+=b, a+=10, a+=14.75e+7
    def __iadd__(self,right):
        if dataType(right) in [str(upNumber.__name__)+'.Number','int','float']:
            tmp=self.__parent+right 
            return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())
        elif dataType(right) in [str(__name__)+'.Number']:
            tmp=self.__parent+right.__parent
            return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())
        else: raise TypeError("Invalid operand of the operator '+='")

    # in-place subtraction operator (-=): a-=b, a-=10, a-=14.75e+7
    def __isub__(self,right):
        if dataType(right) in [str(upNumber.__name__)+'.Number','int','float']:
            tmp=self.__parent-right 
            return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())
        elif dataType(right) in [str(__name__)+'.Number']:
            tmp=self.__parent-right.__parent
            return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())
        else: raise TypeError("Invalid operand of the operator '-='")

    # in-place multiplication operator (*=): a*=b, a*=10, a*=14.75e+7
    def __imul__(self,right):
        if dataType(right) in [str(upNumber.__name__)+'.Number','int','float']:
            tmp=self.__parent*right 
            return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())
        elif dataType(right) in [str(__name__)+'.Number']:
            tmp=self.__parent*right.__parent
            return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())
        else: raise TypeError("Invalid operand of the operator '*='")

    # in-place true division operator (/=): a/=b, a/=10, a/=14.75e+7
    def __itruediv__(self,right):
        if dataType(right) in [str(upNumber.__name__)+'.Number','int','float']:
            tmp=self.__parent/right 
            return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())
        elif dataType(right) in [str(__name__)+'.Number']:
            tmp=self.__parent/right.__parent
            return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())
        else: raise TypeError("Invalid operand of the operator '/='")

    # in-place floor division operator (//=): a//=b, a//=10, a//=14.75e+7
    def __ifloordiv__(self,right):
        if dataType(right) in [str(upNumber.__name__)+'.Number','int','float']:
            tmp=self.__parent//right 
            return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())
        elif dataType(right) in [str(__name__)+'.Number']:
            tmp=self.__parent//right.__parent
            return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())
        else: raise TypeError("Invalid operand of the operator '//='")

    # in-place mod/remainder operator (%=): a%=b, a%=10, a%=14.75e+7
    def __imod__(self,right):
        if dataType(right) in [str(upNumber.__name__)+'.Number','int','float']:
            tmp=self.__parent%right 
            return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())
        elif dataType(right) in [str(__name__)+'.Number']:
            tmp=self.__parent%right.__parent
            return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())
        else: raise TypeError("Invalid operand of the operator '%='")

    # end of in-place operators #
    # --------------------------------------------------------------------

    # --------------------------------------------------------------------
    # Turning standard mathematical functions to methods of Number object
    # --------------------------------------------------------------------
    # To find a.inv()
    def inv(self): return self.__inv__()

    # To find a.fact()
    def fact(self):
        if self.isInteger():
            tmp=psmf.fact(self.__parent)
            return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())
        else: return None

    # To find a.ln(prec); e-based logarithm
    def ln(self,prec=36):
        tmp=psmf.ln(self.__parent,prec)
        return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())

    # To find a.lg(prec); 10-based logarithm
    def lg(self,prec=36):
        tmp=psmf.lg(self.__parent,prec)
        return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())

    # To find a.log(base,prec);
    def log(self,base=10,prec=36):
        if dataType(base) in ['int','float',str(upNumber.__name__)+'.Number']:
            tmp=psmf.log(self.__parent,base,prec)
            return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())
        elif dataType(base)==str(__name__)+'.Number':
            tmp=psmf.log(self.__parent,base.__parent,prec)
            return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())

    # To find e^a, number exponential;
    def exp(self,prec=36):
        tmp=psmf.exp(self.__parent,prec)
        return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())

    # To find square root of a, sqrt(a)
    def sqrt(self,prec=36):
        tmp=psmf.sqrt(self.__parent,prec)
        return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())

    # To find a^2.5, a^b
    def power(self,power=2,prec=36):
        if dataType(power) in ['int','float',str(upNumber.__name__)+'.Number']:
            tmp=psmf.power(self.__parent,power,prec)
            return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())
        elif dataType(power)==str(__name__)+'.Number':
            tmp=psmf.power(self.__parent,power.__parent,prec)
            return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())

    # ------------------------------trigonometric functions-----------------------------
    # To find sine of a, sin(a)
    def sin(self,unit='d',prec=36):
        tmp=psmf.sin(self.__parent,unit,prec)
        return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())

    # To find cosine of a, cos(a)
    def cos(self,unit='d',prec=36):
        tmp=psmf.cos(self.__parent,unit,prec)
        return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())

    # To find tangent of a, tan(a)
    def tan(self,unit='d',prec=36):
        tmp=psmf.tan(self.__parent,unit,prec)
        return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())

    # To find cotangent of a, cot(a)
    def cot(self,unit='d',prec=36):
        tmp=psmf.cot(self.__parent,unit,prec)
        return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())

    # To find secant of a, sec(a)
    def sec(self,unit='d',prec=36):
        tmp=psmf.sec(self.__parent,unit,prec)
        return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())

    # To find cosecant of a, cosec(a)
    def cosec(self,unit='d',prec=36):
        tmp=psmf.cosec(self.__parent,unit,prec)
        return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())

    # To find sine inverse of a, asin(a)
    def asin(self,unit='d',prec=36):
        tmp=psmf.asin(self.__parent,unit,prec)
        return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())

    # To find cosine inverse of a, acos(a)
    def acos(self,unit='d',prec=36):
        tmp=psmf.acos(self.__parent,unit,prec)
        return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())

    # To find tan inverse of a, atan(a)
    def atan(self,unit='d',prec=36):
        tmp=psmf.atan(self.__parent,unit,prec)
        return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())

    # To find cot inverse of a, acot(a)
    def acot(self,unit='d',prec=36):
        tmp=psmf.acot(self.__parent,unit,prec)
        return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())

    # To find sec inverse of a, asec(a)
    def asec(self,unit='d',prec=36):
        tmp=psmf.asec(self.__parent,unit,prec)
        return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())

    # To find cosec inverse of a, acosec(a)
    def acosec(self,unit='d',prec=36):
        tmp=psmf.acosec(self.__parent,unit,prec)
        return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())

    # ------------------------------hyperbolic functions-----------------------------
    # To find hyprbolic sine of a, sinh(a)
    def sinh(self,prec=36):
        tmp=psmf.sinh(self.__parent,prec)
        return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())

    # To find hyprbolic cosine of a, cosh(a)
    def cosh(self,prec=36):
        tmp=psmf.cosh(self.__parent,prec)
        return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())

    # To find hyprbolic tangent of a, tanh(a)
    def tanh(self,prec=36):
        tmp=psmf.tanh(self.__parent,prec)
        return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())

    # To find hyprbolic cotangent of a, coth(a)
    def coth(self,prec=36):
        tmp=psmf.coth(self.__parent,prec)
        return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())

    # To find hyprbolic secant of a, sech(a)
    def sech(self,prec=36):
        tmp=psmf.sech(self.__parent,prec)
        return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())

    # To find hyprbolic cosecant of a, cosech(a)
    def cosech(self,prec=36):
        tmp=psmf.cosech(self.__parent,prec)
        return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())

    # To find hyprbolic sine inverse of a, asinh(a)
    def asinh(self,prec=36):
        tmp=psmf.asinh(self.__parent,prec)
        return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())

    # To find hyprbolic cosine inverse of a, acosh(a)
    def acosh(self,prec=36):
        tmp=psmf.acosh(self.__parent,prec)
        return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())

    # To find hyprbolic tan inverse of a, atanh(a)
    def atanh(self,prec=36):
        tmp=psmf.atanh(self.__parent,prec)
        return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())

    # To find hyprbolic cot inverse of a, acoth(a)
    def acoth(self,prec=36):
        tmp=psmf.acoth(self.__parent,prec)
        return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())

    # To find hyprbolic sec inverse of a, asech(a)
    def asech(self,prec=36):
        tmp=psmf.asech(self.__parent,prec)
        return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())

    # To find hyprbolic cosec inverse of a, acosech(a)
    def acosech(self,prec=36):
        tmp=psmf.acosech(self.__parent,prec)
        return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())          

    # ------------------------------other standard functions-----------------------------
    # gamma(x) function returns approximate value of gamma of x
    # T(z)=Int((t^(z-1))*e^(-t)dt),0,inf)
    def gamma(self,prec=36):
        tmp=psmf.gamma(self.__parent,prec)
        return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())

    # erf(x,prec) returns the integral Int(e^(-t^2)dt) in the interval 
    # from 0 to x with high precision
    # Domain:{R}	Range:{R:-1<=f(x)<=1}
    def erf(self,prec=36):
        tmp=psmf.erf(self.__parent,prec)
        return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())

    # erfc(x,prec) returns the complementary error function of x (1-erf(X))
    # in the interval from 0 to x with high precision
    # Domain:{R}	Range:{R:0<=f(x)<=2}
    def erfc(self,prec=36):
        tmp=psmf.erfc(self.__parent,prec)
        return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())

    # beta(x,y) is called beta function defined by Int(t^(x-1)*(1-t)^(y-1)dt)
    # in the interval [0,1] which is equal to gamma(x)*gamma(y)/gamma(x+y)
    # Domain:{R:x>=0,y>=0}	Range:{R:0<=f(x)<=1}
    def beta(self,y=1,prec=36):
        if dataType(y) in ['int','float',str(upNumber.__name__)+'.Number']:
            tmp=psmf.beta(self.__parent,y,prec)
            return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())
        elif dataType(y)==str(__name__)+'.Number':
            tmp=psmf.beta(self.__parent,y.__parent,prec)
            return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())

    # end of standard mathematical functions #
    # --------------------------------------------------------------------

    # --------------------------------------------------------------------
    # Euler, Bernoulli and Tangent Numbers
    # --------------------------------------------------------------------
    # eulerNumber(r) calculates and returns the euler number of the given positive 
    # integer by double sum method
    def eulerNumber(self):
        if self.isInteger() and self>=0:
            tmp=psmf.eulerNumber(self.__parent)
            return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())
        else: return None

    # bernoulliNumber(r) calculates and returns the Bernoulli number of the given positive 
    # integer (2,4,6,...) by the following definition
    # B(r)=0 if r is an odd positive integer
    def bernoulliNumber(self):
        if self.isInteger() and self>0:
            tmp=psmf.bernoulliNumber(self.__parent)
            return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())
        else: return None

    # tangentNumber(r) calculates and returns the Tangent number of the given positive 
    # and even integer (2,4,6,...) by the following definition
    # T(r)=0 if r is an odd positive integer
    def tangentNumber(self):
        if self.isInteger() and self>0:
            tmp=psmf.tangentNumber(self.__parent)
            return Number(str(tmp)[4:],10,self.getMaxPrecision(),self.isAccurate())
        else: return None















