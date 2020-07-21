from .map import mapv

def get_via_pl(ol,pathlist):
    '''
        from elist.elist import *
        y = ['a',['b',["bb"]],'c']
        y[1][1]
        get_via_pl(y,[1,1])
    '''
    this = ol
    for i in range(0,pathlist.__len__()):
        key = pathlist[i]
        this = this.__getitem__(key)
    return(this)

def get_via_pl2(pathlist,ol):
    '''
        from elist.elist import *
        y = ['a',['b',["bb"]],'c']
        y[1][1]
        get_via_pl2([1,1],y)
    '''
    this = ol
    for i in range(0,pathlist.__len__()):
        key = pathlist[i]
        this = this.__getitem__(key)
    return(this)


def get_via_sibseqs(ol,*sibseqs):
    '''
        from elist.elist import *
        y = ['a',['b',["bb"]],'c']
        y[1][1]
        get_via_sibseqs(y,1,1)
    '''
    pathlist = list(sibseqs)
    this = ol
    for i in range(0,pathlist.__len__()):
        key = pathlist[i]
        this = this.__getitem__(key)
    return(this)


def set_via_pl(ol,pathlist,value):
    '''
        from elist.elist import *
        y = ['a',['b',["bb"]],'c']
        y[1][1]
        setitem_via_pathlist(y,"500",[1,1])
        y
    '''
    this = ol
    for i in range(0,pathlist.__len__()-1):
        key = pathlist[i]
        this = this.__getitem__(key)
    this.__setitem__(pathlist[-1],value)
    return(ol)

def set_via_sibseqs(ol,value,*sibseqs):
    '''
        from elist.elist import *
        y = ['a',['b',["bb"]],'c']
        y[1][1]
        setitem_via_sibseqs(y,"500",1,1)
        y
    '''
    this = ol
    pathlist = list(sibseqs)
    for i in range(0,pathlist.__len__()-1):
        key = pathlist[i]
        this = this.__getitem__(key)
    this.__setitem__(pathlist[-1],value)
    return(ol)


def del_via_pl(ol,pathlist):
    '''
        from elist.elist import *
        y = ['a',['b',["bb"]],'c']
        y[1][1]
        delitem_via_pathlist(y,[1,1])
        y
    '''
    this = ol
    for i in range(0,pathlist.__len__()-1):
        key = pathlist[i]
        this = this.__getitem__(key)
    this.__delitem__(pathlist[-1])
    return(ol)


def del_via_sibseqs(ol,*sibseqs):
    '''
        from elist.elist import *
        y = ['a',['b',["bb"]],'c']
        y[1][1]
        delitem_via_sibseqs(y,1,1)
        y
    '''
    pathlist = list(sibseqs)
    this = ol
    for i in range(0,pathlist.__len__()-1):
        key = pathlist[i]
        this = this.__getitem__(key)
    this.__delitem__(pathlist[-1])
    return(ol)




def set_via_il_vl(ol,indexes,values):
    for i in range(indexes.__len__()):
        ol[i] = values[i]
    return(ol)

def set_via_ivlist(ol,*iv_tuples):
    iv_tuples = list(iv_tuples)
    for t in iv_tuples:
        ol[t[0]] = t[1]
    return(ol)


def pl_to_bracket_str(path_list):
    '''
        >>> pl_to_bracket_str([1, '1', 2])
            "[1]['1'][2]"
        >>>
    '''
    t1 = path_list.__repr__()
    t1 = t1.lstrip('[')
    t1 = t1.rstrip(']')
    t2 = t1.split(", ")
    s = ''
    for i in range(0,t2.__len__()):
        s = ''.join((s,'[',t2[i],']'))
    return(s)



def bracket_str_to_pl(gs):
    '''
        gs = "[1]['1'][2]"
        bracket_str_to_pl(gs)
        gs = "['u']['u1']"
        bracket_str_to_pl(gs)
    '''
    def numize(w):
        try:
            int(w)
        except:
            try:
                float(w)
            except:
                return(w)
            else:
                return(float(w))
        else:
           return(int(w))
    def strip_quote(w):
        if(type(w) == type('')):
            if(w[0]==w[-1]):
                if((w[0]=="'") |(w[0]=='"')):
                    return(w[1:-1])
                else:
                    return(w)
            else:
                return(w)
        else:
            return(w)
    gs = gs[1:-1]
    pl = gs.split("][")
    pl = mapv(pl,numize)
    pl = mapv(pl,strip_quote)
    return(pl)



