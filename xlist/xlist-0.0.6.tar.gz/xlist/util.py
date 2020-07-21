from .slct  import some_keeping_order,some
from .index import uniform_index

def fcp(ol):
    return(ol[:])


def max_length(ol):
    lngths = list(map(lambda r:len(r),ol))
    lngth = max(lngths)
    return(lngth)


def entries(ol):
    rslt = []
    length = ol.__len__()
    for i in range(0,length):
        entry = [i,ol[i]]
        rslt.append(entry)
    return(rslt)


def includes(ol,value):
    return((value in ol))


def to_str(ol):
    return(ol.__str__())


def to_src(ol):
    return(ol.__repr__())


def every(ol,test_func,*args,**kwargs):
    rslt = True
    length = ol.__len__()
    for i in range(0,length):
        cond = test_func(ol[i],*args)
        if(cond):
            pass
        else:
            return(False)
    return(rslt)


def any(ol,test_func,*args,**kwargs):
    rslt = False
    length = ol.__len__()
    for i in range(0,length):
        cond = test_func(ol[i],*args)
        if(cond):
            return(True)
        else:
            pass
    return(rslt)


def uniqualize(l,**kwargs):
    if('mode' in kwargs):
        mode = kwargs['mode']
    else:
        mode = 'deepcopy'
    pt = copy.deepcopy(l)
    seqs =[]
    freq = {}
    for i in range(0,pt.__len__()):
        v = pt[i]
        if(v in freq):
            freq[v] = freq[v] + 1
        else:
            freq[v] = 0
            seqs.append(i)
    #####下面是影响速度的关键,append特别耗时
    #npt = some_keeping_order(pt,*seqs)
    npt = some(pt,*seqs)
    ########################
    pt = npt
    if(mode == 'deepcopy'):
        return(npt)
    else:
        l.clear()
        l.extend(npt)
        return(l)

def combinations(arr,*args):
    args = list(args)
    lngth = len(args)
    if(lngth == 0):
        start = 1
        end = len(arr) + 1
    elif(lngth == 1):
        start = uniform_index(args[0],lngth)
        end = len(arr) + 1
    else:
        start = uniform_index(args[0],lngth)
        end = uniform_index(args[1],lngth)
    rslt = []
    for i in range(start,end):
        tmp = list(itertools.combinations(arr,i))
        rslt.extend(tmp)
    return(rslt)

