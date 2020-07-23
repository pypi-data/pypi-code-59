from .cmmn import dflt_kwargs
from .map import mapiv

def vil_dict(l):
    st = set({})
    rslt = {}
    for i in range(len(l)):
        v = l[i]
        if(v in st):
            rslt[v].append(i)
        else:
            st.add(v)
            rslt[v] = [i]
    return(rslt)


def ivdict(ol):
    d = {}
    for i in range(ol.__len__()):
        d[i] = ol[i]
    return(d)

def vidict(arr):
    d = {}
    for i in range(arr.__len__()):
        d[arr[i]] = i
    return(d)

def mirror_dict(arr):
    d = {}
    for i in range(arr.__len__()):
        d[i] = arr[i]
        d[arr[i]] = i
    return(d)


def table(l,**kwargs):
    iname = dflt_kwargs("iname","index",**kwargs)
    vname =  dflt_kwargs("vname","value",**kwargs)
    dl = mapiv(l,lambda i,v:{iname:i,vname:v})
    return(dl)


def vil_dict_after_vtrans(l,*other_args,trans_func=lambda r:r):
    desc = {}
    for i in range(0,l.__len__()):
        ele = l[i]
        nv = trans_func(ele,*other_args)
        if(nv in desc):
            desc[nv].append(i)
        else:
            desc[nv] = [i]
    return(desc)    


