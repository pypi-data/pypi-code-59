import copy
import functools


def deepcopy_wrapper(func):
    @functools.wraps(func)
    def wrapper(ol,*args,**kwargs):
        deepcopy = kwargs['deepcopy'] if('deepcopy' in kwargs) else True
        nl = copy.deepcopy(ol) if(deepcopy) else ol
        rslt = func(nl,*args,**kwargs)
        return(rslt)
    return(wrapper)

def keep_ptr_replace(ol,nl):
    ol.clear()
    ol.extend(nl)
    return(ol)


def inplace_wrapper(func):
    @functools.wraps(func)
    def wrapper(ol,*args,**kwargs):
        deepcopy = kwargs['deepcopy'] if('deepcopy' in kwargs) else True
        nl = copy.deepcopy(ol)
        nl = func(nl,*args,**kwargs)
        rslt = nl if(deepcopy) else keep_ptr_replace(ol,nl)
        return(rslt)
    return(wrapper)


def identity(obj):
    return(obj)



def dflt_kwargs(k,dflt,**kwargs):
    if(k in kwargs):
        v = kwargs[k]
    else:
        v = dflt
    return(v)



class _Undefined():
    def __repr__(self):
        return('undefined')

class _Null():
    def __repr__(self):
        return(null)



undefined = _Undefined()
null = _Null()

