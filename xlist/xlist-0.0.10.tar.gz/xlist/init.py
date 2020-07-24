from .cmmn import deepcopy_wrapper
from .cmmn import inplace_wrapper
from .cmmn import identity
import copy
import inspect
from .slct import odds,evens


def init(lngth,*args,**kwargs):
    deepcopy = kwargs['deepcopy'] if('deepcopy' in kwargs) else True
    dflt_ele = args[0] if(len(args)>0) else None
    rslt = []
    for i in range(0,lngth):
        dflt_ele = copy.deepcopy(dflt_ele) if(deepcopy) else dflt_ele
        rslt.append(dflt_ele)
    return(rslt)

def from_range(si,ei,step=1):
    return(list(range(si,ei,step)))


@inplace_wrapper
def fill(ol,value,si=None,ei=None,**kwargs):
    lngth = len(ol)
    si = 0 if(si==None) else si
    ei = lngth if(ei==None) else ei
    for i in range(si,ei):
        ol[i] = value
    return(ol)


@deepcopy_wrapper
def lfrom(obj,*args,**kwargs):
    func = args[0] if(len(args)>0) else identity
    spec = inspect.getargspec(func)
    params_lngth = len(spec.args)
    has_args = (spec.varargs!=None)
    has_kw = (spec.keywords!=None)
    other_args = args[1:] 
    ol = list(obj)
    nl = []
    for i in range(len(ol)):
        if(params_lngth==1 and has_args and has_kw):
            ele = func(ol[i],*other_args,**kwargs)
        elif(params_lngth==1 and has_args and not(has_kw)):
            ele = func(ol[i],*other_args)
        elif(params_lngth==1 and not(has_args) and has_kw):
            ele = func(ol[i],**kwargs)
        elif(params_lngth==1 and not(has_args) and not(has_kw)):
            ele = func(ol[i])
        elif(params_lngth==2 and has_args and has_kw):
            ele = func(ol[i],i,*other_args,**kwargs)
        elif(params_lngth==2 and has_args and not(has_kw)):
            ele = func(ol[i],i,*other_args)
        elif(params_lngth==2 and not(has_args) and has_kw):
            ele = func(ol[i],i,**kwargs)
        elif(params_lngth==2 and not(has_args) and not(has_kw)):
            ele = func(ol[i],i)
        else:
            raise(TypeError("type error!")) 
        nl.append(ele)
    return(nl)



def of(*eles):
    return(list(eles))




def from_one_list(ol,*args,**kwargs):
    nl = ol
    args = list(args)
    if(isinstance(args,list)):
        indexes = args[0]
        values = args[1]
    else:
        indexes = slct.odds(ol)
        values = slct.evens(ol)
    lngth = indexes.__len__()
    for i in range(lngth):
        index = indexes[i]
        value = values[i]
        nl[index] = value
    return(nl)
