from operator import itemgetter


def some(ol,*indexes):
    if(indexes.__len__()==0):
        rslt = []
    else:
        rslt = itemgetter(*indexes)(ol)
        rslt = list(rslt)
    return(rslt)

def some_keeping_order(ol,*indexes):
    rslt = []
    for i in range(0,indexes.__len__()):
        index = indexes[i]
        ele = ol[index]
        rslt.append(ele)
    return(rslt)


def not_some(ol,*indexes):
    lngth = len(ol)
    all_index_st = set(list(range(0,lngth,1)))
    unslcted_index_st = set(indexes)
    slcted_index_st = all_index_st.difference(unslcted_index_st)
    slcted_indexes = list(slcted_index_st)
    rslt = some(ol,*slcted_indexes)
    return(rslt)


def car(ol):
    return(ol[0])

def cdr(ol):
    return(ol[1:])

def head(ol):
    return(ol[0])

def tail(ol):
    return(ol[1:])

def init(ol):
    return(ol[:-1])

def last(ol):
    return(ol[-1])


def preceding(ol,index):
    return(ol[0:index])

def following(ol,index):
    return(ol[index+1:len(ol)])

def via_range(ol,si,ei):
    return(ol[si:ei])


def odds(ol):
    nl = []
    for i in range(0,ol.__len__()):
        if((i%2)!=0):
            nl.append(ol[i])
        else:
            pass
    return(nl)    

def evens(ol):
    nl = []
    for i in range(0,ol.__len__()):
        if((i%2)==0):
            nl.append(ol[i])
        else:
            pass
    return(nl)


def interval(ol,interval,**kwargs):
    si = kwargs['si'] if('si' in kwargs) else 0
    ei = kwargs['ei'] if('ei' in kwargs) else len(ol)
    nl = []
    lngth = ol.__len__()
    for i in range(si,lngth):
        if((i%interval)==0):
            nl.append(ol[i])
        else:
            pass
    return(nl)


