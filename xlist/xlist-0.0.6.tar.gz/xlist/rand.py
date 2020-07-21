import random
import copy

def rand_some_indexes(si,ei,n,**kwargs):
    if('sort' in kwargs):
        sort = kwargs['sort']
    else:
        sort = True
    rslt = []
    arr = init_range(si,ei,1)
    c = 0
    while(c<n):
        r = random.randrange(0,ei)
        p = arr.pop(r)
        rslt.append(p)
        ei = ei - 1
        c = c + 1
    if(sort):
        rslt.sort()
    else:
        pass
    return(rslt)


def rand_sub(arr,*args,**kwargs):
    arr = copy.deepcopy(arr)
    lngth = arr.__len__()
    args = list(args)
    if(args.__len__() == 0):
        n = random.randrange(0,lngth)
    else:
        n = args[0]
        if(n>lngth):
            n = lngth
        else:
            pass
    indexes = rand_some_indexes(0,lngth,n,**kwargs)
    narr = some_keeping_order(arr,*indexes)
    return(narr)

