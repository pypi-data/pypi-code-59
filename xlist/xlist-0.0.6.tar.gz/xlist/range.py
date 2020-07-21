from .map   import mapv
from .init  import from_range 
from .cmmn  import inplace_wrapper
from .index import uniform_index,indexes_all
from .sort  import sort_refer_to
from .fltr  import fltrv


def compress(ol):
    '''
        #only support sorted-ints or sorted-ascii
        l = [1,5,6,7,8,13,14,18,30,31,32,33,34]
        compress(l)
        l = [1,5,6,7,8,13,14,18,30,31,32,33,34,40]
        compress(l)
        l = ['a','b','c','d','j','k','l','m','n','u','y','z']
        compress(l)
    '''
    T = (type(ol[0]) == type(0))
    if(T):
        l = ol
    else:
        l = mapv(ol,ord)
    length = l.__len__()
    secs = []
    si = 0
    ei = 0
    prev = l[0]
    for i in range(1,length):
        curr = l[i]
        cond = (curr == (prev+1))
        if(cond):
            ei = i
            prev = curr
        else:
            if(T):
                sec = (l[si],l[ei])
            else:
                sec = (ol[si],ol[ei])
            if(si == ei):
                sec = sec[0]
            else:
                pass
            secs.append(sec)
            si = i
            ei = i
            prev = curr
    if(T):
        sec = (l[si],l[ei])
    else:
        sec = (ol[si],ol[ei])
    if(si == ei):
        sec = sec[0]
    else:
        pass
    secs.append(sec)
    return(secs)




def decompress(cl):
    '''
        #only support sorted-ints or sorted-ascii
        cl = [1, (5, 8), (13, 14), 18, (30, 34)]
        decompress(cl)
        cl = [1, (5, 8), (13, 14), 18, (30, 34), 40]
        decompress(cl)
        cl = [('a', 'd'), ('j', 'n'), 'u', ('y', 'z')]
        decompress(cl)
    '''
    def cond_func(ele):
        length = ele.__len__()
        cond = (length == 1)
        if(cond):
            return(ord(ele))
        else:
            x = ord(ele[0])
            y = ord(ele[1])
            return((x,y))
    if(type(cl[0])==type(0)):
        T = True
    elif(cl[0].__len__() == 1):
        T = (type(cl[0]) == type(0))
    else:
        T = (type(cl[0][0]) == type(0))
    if(T):
        l = cl
    else:
        l = mapv(cl,cond_func)
    rslt = []
    for i in range(0,l.__len__()):
        ele = l[i]
        if(type(ele) == type(0)):
            arr = [ele]
        elif(ele.__len__() == 1):
            arr = [ele]
        else:
            sv = ele[0]
            ev = ele[1]
            arr = from_range(sv,ev+1,1)
        if(T):
            pass
        else:
            arr = mapv(arr,chr)
        rslt.extend(arr)
    return(rslt)





def spanize(break_points,length):
    bps = mapv(break_points,uniform_index,length)
    bps.sort()
    bps = prepend(bps,0)
    bps = append(bps,length)
    bps = uniqualize(bps)
    bpslen = bps.__len__()
    secs=[(0,bps[0])]
    for i in range(0,bpslen-1):
        r = (bps[i],bps[i+1])
        secs.append(r)
    secs.append((bps[bpslen-1],length))
    if(secs[0][0] == secs[0][1]):
        secs.pop(0)
    else:
        pass
    if(secs[-1][0] == secs[-1][1]):
        secs.pop(-1)
    else:
        pass
    return(secs)


def fullfill_spans(spans,lngth):
    brkpnts = []
    for i in range(0,spans.__len__()):
        span = spans[i]
        brkpnts.append(span[0])
        brkpnts.append(span[1])
    return(spanize(brkpnts,lngth))


def get_supplement_of_spans(spans,lngth):
    rslt = []
    si = 0
    ei = spans[0][0]
    if(si == ei):
        pass
    else:
        rslt.append((si,ei))
    prev_ei = spans[0][1]
    for i in range(1,spans.__len__()):
        si = prev_ei
        ei = spans[i][0]
        rslt.append((si,ei))
        prev_ei = spans[i][1]
    if(prev_ei < lngth):
        rslt.append((prev_ei,lngth))
    else:
        rslt.append((prev_ei,lngth+1))
    rslt = fltrv(rslt,lambda r:r[0]!=r[1])
    return(rslt)


def get_span_loc(spans,word_loc):
    for i in range(0,spans.__len__()):
        span = spans[i]
        if((word_loc>=span[0])&(word_loc<span[1])):
            return(i)
        else:
            pass
    return(None)




def broke_via_seqs(ol,break_points):
    bps = list(break_points)
    length = ol.__len__()
    rgs = spanize(bps,length)
    rslt = []
    for i in range(0,rgs.__len__()):
        si,ei = rgs[i]
        sec = ol[si:ei]
        rslt.append(sec)
    return(rslt)



def broke_via_some(ol,*break_points):
    bps = list(break_points)
    return(broke_via_seqs(ol,bps))



def where_index_interval(ol,value):
    si = None
    ei = None
    for i in range(0,ol.__len__()):
        ele = ol[i]
        if(value >ele):
            si = i
        elif(value == ele):
            return((i,i))
        else:
            ei = i
            return((si,ei))
    return((si,ei))



def where_value_interval(ol,value):
    '''
        ol = [0, 4, 6, 8, 10, 14]
        value_interval(ol,-1)
        value_interval(ol,1)
        value_interval(ol,2)
        value_interval(ol,3)
        value_interval(ol,4)
        value_interval(ol,9)
        value_interval(ol,14)
        value_interval(ol,17)
    '''
    si,ei = where_index_interval(ol,value)
    if(si == None):
        sv = None
    else:
        sv = ol[si]
    if(ei == None):
        ev = None
    else:
        ev = ol[ei]
    return((sv,ev))


def upper_bound(ol,value):
    return(where_value_interval(ol,value)[1])

def lower_bound(ol,value):
    return(where_value_interval(ol,value)[0])



def chunk(ol,interval):
    length = ol.__len__()
    seqs = from_range(0,length,interval)
    rslt = broke_via_seqs(ol,seqs)
    return(rslt)

